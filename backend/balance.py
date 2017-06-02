#encoding=utf-8

import models
from base import Base


class BalanceManager(Base):
    def __init__(self, logger_name):
        super(BalanceManager, self).__init__(logger_name)


    def top_up(self, message):
        # Parser the parameters
        user_id = message['json_content']['user_id']
        amount = message['json_content']['amount']


        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 


        # Updade the database
        new_balance = check['balance'] + amount
        try:
            self.sql.update_one(models.User,
                                     {'id':user_id},
                                     {'balance':new_balance})
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The user's balance has been update." % (self.msg_success)
        self.log.info(response)

        return self._response({"balance":new_balance}, True)


    def withdraw(self, message):
        # Parser the parameters
        user_id = message['json_content']['user_id']
        amount = message['json_content']['amount']


        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 


        # Updade the database
        if check['balance'] < amount:
            response = "%s The balance is insufficient." % (self.msg_success)
            self.log.info(response)
            return self._response(response)

        new_balance = check['balance'] - amount 
        try:
            self.sql.update_one(models.User,
                                     {'id':user_id},
                                     {'balance':new_balance})
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The user's balance has been update." % (self.msg_success)
        self.log.info(response)

        return self._response({"balance":new_balance}, True)


    def get_balance(self, message):
        # Parser the parameters
        user_id = message['url_content']['id'][0]

        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        balance = check['balance']

        # Response
        msg = "%s . Get the balance successfully" % (self.msg_success)
        self.log.info(msg)

        return self._response({"balance":balance}, True)

