#encoding=utf-8

import models
from base import Base

import datetime

class OrderManager(Base):
    def __init__(self, logger_name):
        super(OrderManager, self).__init__(logger_name)


    def generate_order(self, message):
        # Parser the parameters
        user_id = message['json_content']['user_id']
        pay_amount = message['json_content']['pay_amount']
        book_list = message['json_content']['book_list']
        order_status = message['json_content']['status']



        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Generage_order_serial_number
        sn = str(datetime.datetime.now())
        sn = sn.replace('-','').replace(' ','').replace(':','').replace('.','')


        # Updade the database
        
        try:
             order_id = self.sql.insert(models.Order,
                                        user_id = user_id,
                                        serial_number = sn,
                                        pay_amount = pay_amount,
                                        book_list = str(book_list),
                                        status = order_status)
             if not order_id:
                 raise AttributeError("Failed to insert order's information")
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The order has been generated successfully." % (self.msg_success)
        self.log.info(response)

        return self._response({"order_id":order_id}, True)


    def get_order_details(self, message):
        # Parser the parameters
        user_id = message['url_content']['user_id'][0]


        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        response = []
        try:
            orders = self.sql.query(models.Order,
                                    user_id=user_id)
            if not orders:
                raise AttributeError("No orders (user_id:%s)" % user_id)
            for order in orders:
                try:
                    temp = dict()
                    temp['id'] = order['id']
                    temp['serial_number'] = order['serial_number']
                    temp['created_at'] = order['created_at']
                    temp['pay_amount'] = order['pay_amount']
                    temp['status'] = order['status']
                    temp['book_list'] = eval(order['book_list'])
                    book_cover = list()
                    for book_id in eval(order['book_list']):
                        book = self.sql.query_one(models.Book, id=book_id)
                        book_cover.append(book['cover'])
                    temp['cover_list'] = book_cover
                    response.append(temp)
                except Exception as e:
                    self.log.error(e)
                    pass
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))

        # Response
        msg = "%s Get user's orders successfully." % (self.msg_success)
        self.log.info(msg)

        return self._response(response, True)


    def update_order_status(self, message):
        # Parser the parameters
        user_id = message['json_content']['user_id']
        order_id = message['json_content']['order_id']
        new_status = message['json_content']['order_status']

        # Check whether the order exists.
        check = self.sql.query_one(models.Order, id=order_id)
        if not check:
            msg_f = "%s. Info:The order does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 


        # Updade the database
        
        try:
             self.sql.update_one(models.Order,
                             {'id':order_id},
                             {'status':new_status})
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))

        # Response
        msg = "%s . Get the balance successfully" % (self.msg_success)
        self.log.info(msg)

        return self._response(msg, True)



    def delete_order(self, message):
        # Parser the parameters
        order_id_list = message['json_content']['order_id_list']
 
        try:
            for order_id in order_id_list:
                try:
                    self.sql.delete_one(models.Order, id=order_id)
                except Exception as e:
                    pass
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        # Response
        response = "%s The orders has been removed." % (self.msg_success)
        self.log.info(response)

        return self._response(response, True)


