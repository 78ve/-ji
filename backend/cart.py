#encoding=utf-8

import models
from base import Base


class CartManager(Base):
    def __init__(self, logger_name):
        super(CartManager, self).__init__(logger_name)


    def handle_results(self, instances):
        res = list()
        for instance in instances:
            d = instance.__dict__
            del(d['_sa_instance_state'])
            res.append(d)
        return res

    def insert_book(self, message):
        # Parser the parameters
        book_id = message['url_content']['book_id'][0]
        user_id = message['url_content']['user_id'][0]
        quantity = message['url_content']['qty'][0]


        # Check whether the user exists.
        check = self.sql.query_one(models.Cart, book_id=book_id, user_id=user_id)
        if check:
            msg_f = "%s. Info:The book has already existed" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 


        # Insert into the database
        try:
            id = self.sql.insert(models.Cart,
                                 user_id=user_id,
                                 book_id=book_id,
                                 quantity=quantity)
            if not id:
                raise AttributeError("Failed to insert into the database")
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The books(id:%s) has been added into user's(id:%s) cart." % (self.msg_success, book_id, user_id)
        self.log.info(response)

        return self._response(response, True)



    def delete_book(self, message):
        # Parser the parameters
        cart_item_id = message['url_content']['id'][0]

        # Insert into the database
        try:
            self.sql.delete_one(models.Cart, id=cart_item_id)
            if not id:
                raise AttributeError("Failed to delete the item(%s)" % cart_item_id)
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The item(id:%s) has been removed from the cart." % (self.msg_success, cart_item_id)
        self.log.info(response)

        return self._response(response, True)



    def get_cart(self, message):
        # Parser the parameters
        user_id = message['url_content']['id'][0]

        response = []
        # Insert into the database
        try:
            cart_items = self.sql.query(models.Cart, user_id=user_id)
            if not cart_items:
                raise AttributeError("No books in the cart(user_id:%s)" % user_id)
            for item in cart_items:
                try:
                    temp = dict()
                    temp['id'] = item['id']
                    temp['quantity'] = item['quantity']
                    book = self.sql.query_one(models.Book, id=item['book_id'])
                    temp['book_id'] = item['book_id']
                    temp['name'] = book['name']
                    temp['cover'] = book['cover']
                    temp['price'] = book['price']
                    temp['selected'] = True
                    response.append(temp)
                except Exception as e:
                    self.log.error(e)
                    pass
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        msg = "%s. Results:%s" % (self.msg_success, str(response))
        self.log.info(msg)

        return self._response(response, True)

