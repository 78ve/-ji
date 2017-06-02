
from contextlib import contextmanager
import inspect
import functools
import sqlalchemy
from .orm_wrapper import Session, Query, get_maker

'''
In order to get the decorators, user should do such things:

.. code-block:: python

  provider = get_connection_provider(sqlbackend)
  configure_provider(provider)
  writer = get_writer()
  reader = get_reader()

Then you can use writer and reader as decorators.
'''

class _symbol(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'symbol(%r)' % self.name

_ASYNC_READER = _symbol('ASYNC_READER')
_READER = _symbol('READER')
_WRITER = _symbol('WRITER')

class SessionContext(object):
    pass


class ConnectionProvider(object):
    '''This Connection Provider doesn't only provide the sqlalchemy "connection",
    it is an object that stores all information used to connect to sqlbackend.
    It also maintains references to sqlalchemy connection, session, transaction,
    sessionmaker, etc.that will be used in programs.'''

    def __init__(self, sqlbackend):

        # the real string used to connect to the sqlbackend
        self.sqlbackend = sqlbackend
        self._started = False

    def _start(self, maker_kwargs):
        if self._started:
            return

        self._engine = sqlalchemy.create_engine(self.sqlbackend, echo=False)
        self._session_maker = get_maker(engine = self._engine, **maker_kwargs)
        self._started = True

    def create_connection(self):
        if not self._started:
            self._start(maker_kwargs={})
        return self._engine.connect()

    def create_session(self, mode, bind=None):
        if not self._started:
            self._start(maker_kwargs={})
        kw = {}

        # In case that you need to bind the session to another engine
        if bind:
            kw['bind'] = bind
        return self._session_maker(**kw)


def get_connection_provider(sqlbackend):
    '''Get a ConnectionProvider object by database backend'''
    return ConnectionProvider(sqlbackend)


class TransactionContext(object):
    '''A TransactionContext represents a single transaction in progress.
     This transaction can be a transaction contained by a session or a transaction object in sqlalchemy.
     This transaction can be a outer transaction or a subtransaction.
     It just make effect on when to commit the transaction or when to rollback it.
     It is a callable object, the __call__ method is a decorator, thus make a TransactionContext object a decorator.
     Decorating a function with it, means all operation of the function was included in the Transaction.'''

    def __init__(self, provider = None, root=None, mode=_READER):

        if root is None:
            self._root = self
            self._independent = True
        else:
            self._root = root
            self._independent =False

        self._provider = provider
        self._mode = mode

        self.session = None
        self.connection = None
        self.transaction = None

    def configure_provider(self, provider):
        self._provider = provider

    def __call__(self, func):
        '''Decorate a function.'''
        argspec = inspect.getargspec(func)
        if argspec.args[0] == ('self' or 'cls'):
            context_index = 1
        else:
            context_index = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            '''Get the context parameter in args we passed to the decorated function.'''
            if 'context' in kwargs:
                context = kwargs['context']
            else:
                context = args[context_index]
                with self._transaction_scope(context):
                    return func(*args, **kwargs)
        return wrapper

    @contextmanager
    def _connection(self):
        '''Not Often Used.'''
        self.transaction = self.connection.begin(subtransactions=True)
        try:
            yield self.connection
            self._end_transaction(self.transaction)
        except Exception:
            self.transaction.rollback()
            raise
        finally:
            self.transaction = None
            self.connection.close()

    @contextmanager
    def _session(self):
        '''Usually use this rather than _connection().'''
        if self.session is None:
            self.session = self._provider.create_session(bind=self.connection, mode=self._mode)
            try:
                self.session.begin(subtransactions=True)
                yield self.session
                self._end_transaction(self.session)
            except Exception as e:
                self.session.rollback()
                raise
            finally:
                self.session.close()
                self.session = None
        else:
            yield self.session

    def _end_transaction(self, s_t):
        '''s_t means session or transaction. The operation to session and transaction are the same.'''
        if self._mode is _WRITER:
            try:
                s_t.commit()
            except Exception as e:
                print(e)
        else:
            s_t.rollback()

    def _produce_block(self):
        ''' Well in this produce_block, I will'''
        if self.connection:
            return self._connection()
        else:
            return self._session()

    @contextmanager
    def _transaction_scope(self, context):
        '''All the things to do with transaction goes here.'''

        if self._mode is not None:
            with self._produce_block() as resource:
                # In there we give the user-defined context the session attribute
                context.session = resource
                yield
        else:
            yield


    def _clone(self, mode):
        if self._root  == self:
            root = None
        else:
            root = self._root

        provider = self._provider

        return TransactionContext(provider, root, mode=mode)

    def _get_reader(self):
        return self._clone(mode=_READER)

    def _get_writer(self):
        return self._clone(mode=_WRITER)




_theTransactionContext = TransactionContext()

# reader = _theTransactionContext._get_reader()

# writer = _theTransactionContext._get_writer()


get_writer = lambda:_theTransactionContext._get_writer()

get_reader = lambda:_theTransactionContext._get_reader()



def configure_provider(provider):
    global _theTransactionContext
    _theTransactionContext.configure_provider(provider)

