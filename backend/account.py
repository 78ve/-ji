import hashlib
import models
from base import Base


class AccountsManager(Base):
    def __init__(self, logger_name):
        super(AccountsManager, self).__init__(logger_name)



    def spilt_users(self, users, items=4):
        response = []
        len_user = len(users)
        if len_user < items:
            response.append(users)
        else:
            for i in range(0, len_user, items):
                response.append(users[i:i+items])
        return response


    def create(self, message):
        # parser the parameters
        user_info = message['json_content']


        # Check whether the username is duplicated.
        check = self.sql.query(models.User, name=user_info['username'])
        if check:
            msg_f = "%s. Info:The user exists" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Encrypt the password
        encrypt = hashlib.md5()
        encrypt.update(user_info['password'].encode(encoding='utf-8'))
        password = encrypt.hexdigest()


        try:
            # Insert the user's infomation into the database
            user_id = self.sql.insert(models.User,
                       name=user_info['username'].encode(encoding='utf-8'),
                       passwd=password,
                       userLevel = user_info.get('userLevel', 0),
                       balance=0)
            if not user_id:
                raise AttributeError("Failed to insert user's information")
            response = {"user_id":user_id,
                        "username":user_info['username'],
                        "userLevel":user_info.get('userLevel', 0)}
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))
        
        # Response 
        self.log.info("%s The account(username:%s) has been created." % (self.msg_success, user_info['username'])) 

        return self._response(response, True) 


    def update(self, message):
        # Parser the parameters
        filter = message['json_content']['user_id']
        password = message['json_content']['password']
        encrypt = hashlib.md5()
        encrypt.update(password.encode(encoding='utf-8'))
        password = encrypt.hexdigest()
    
        update_info = message['json_content']['update_info']

        # Check whether the user exists.
        check = self.sql.query(models.User, id=filter)
        if not check:
            msg_f = "%s. Info:The user does not exists" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Check whether the password is valid.
        try:
            password_t = self.sql.query_one(models.User,
                                          id=filter)['passwd']
            if password_t != password:
                msg_f = "%s. Info:The password is not correct" % self.msg_failed
                self.log.error(msg_f)
                return self._response(msg_f)
        except Exception as e:
            msg_f = "%s. Info:Failed to check the password" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f)
    
        # Update the information of the account
        try:
            self.sql.update_one(models.User,
                                {"id":filter},
                                update_info)
        except Exception as e:
            msg_f = "%s. Info:Failed to update the account's information" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f)

        # Response 
        response = "%s The account(id:%s) has been updated." % (self.msg_success, filter)
        self.log.info(response) 

        return self._response(response, True) 


    def delete(self, message):
        # Parser the parameters
        user_id = message['url_content']['user_id'][0]

        # Check whether the user exists.
        check = self.sql.query_one(models.User, id=user_id)
        if not check:
            msg_f = "%s. Info:The user does not exists" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Delete the account
        try:
            self.sql.delete_one(models.User, id=user_id)
        except Exception as e:
            msg_f = "%s. Info:Failed to delete the account. Info:%s" % (self.msg_failed, str(e))
            self.log.error(msg_f)
            return self._response(msg_f)

        # Response 
        response = "%s The account(id:%s) has been deleted." % (self.msg_success, user_id)
        self.log.info(response) 

        return self._response(response, True) 

    def login_check(self, message):
        # Parser the parameters
        username = message['url_content']['username'][0]
        token = message['url_content']['token'][0]

        # Check whether the user exists.
        check = self.sql.query_one(models.User, name=username)
        if not check:
            msg_f = "%s. Info:The user does not exists" % self.msg_failed
            self.log.error(msg_f)
            return self._response(msg_f) 

        # Check whether the password is valid.
        try:
            password_t = check['passwd']
            if password_t != token:
                msg_f = "%s. Info:The password is not correct" % self.msg_failed
                self.log.error(msg_f)
                return self._response(msg_f)
        except Exception as e:
            msg_f = "%s. Info:%s" % (self.msg_failed, str(e))
            self.log.error(msg_f)
            return self._response(msg_f)

        # Response 
        response = "%s The account(username:%s)has logined successfully." % (self.msg_success, username)
        self.log.info(response) 

        return self._response({"user_id":check['id'],"userLevel":check['userLevel']}, True) 



    def get_all_users(self, message):
        # Parser the parameter

        leng = 0
        
        # Get Books
        try:
            users = self.sql.query(models.User)
            if not users:
                return self._response("Data Not Found")
            leng = len(users)
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        response = self.spilt_users(users, items=10)
        self.log.info("Get users successfully")

        # Response
        return self._response(response, success=True, len=leng)


