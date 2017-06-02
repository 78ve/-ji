#encoding=utf-8

import models
from base import Base


class CommentManager(Base):
    def __init__(self, logger_name):
        super(CommentManager, self).__init__(logger_name)


    def generate_comment(self, message):
        # Parser the parameters
        user_id = message['json_content']['user_id']
        book_list = message['json_content']['book_list']
        rate = float(message['json_content']['rate'])
        comment = message['json_content']['comment']



        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Generage_order_serial_number
        for book_id in book_list:
            book = self.sql.query_one(models.Book, id=book_id)
            old_rate = float(book['rate'])
            rate_number = book['rateNumber']
            new_rate = old_rate * (rate_number/(rate_number+1)) + rate * (1/(rate_number+1))
            try:
                 order_id = self.sql.insert(models.Comment,
                                            user_id = user_id,
                                            book_id = book_id,
                                            rate = new_rate,
                                            comment = comment)
                 if not order_id:
                     raise AttributeError("Failed to insert order's information")
                 self.sql.update_one(models.Book,
                                     {"id":book_id},
                                     {"rate":new_rate,
                                      "rateNumber":rate_number + 1})
            except Exception as e:
                self.log.error(e)
                pass

        # Response
        response = "%s The comment has been generated successfully." % (self.msg_success)
        self.log.info(response)

        return self._response(response, True)


    def get_comments(self, message):
        # Parser the parameters
        book_id = message['url_content']['book_id'][0]


        # Check whether the book exists.
        check = self.sql.query_one(models.Book, id=book_id)
        if not check:
            msg_f = "%s. Info:The user does not exist" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        response = []
        try:
            comments = self.sql.query(models.Comment,
                                     book_id=book_id)
            for comment in comments:
                try:
                    temp = dict()
                    temp['created_at'] = comment['created_at']
                    temp['content'] = comment['comment']
                    temp['username'] = self.sql.query_one(models.User, id=comment['user_id'])['name']
                    response.append(temp)
                except Exception as e:
                    self.log.error(e)
                    pass
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))

        # Response
        msg = "%s Get book's comments successfully." % (self.msg_success)
        self.log.info(msg)

        return self._response(response, True)

