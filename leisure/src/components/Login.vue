<template>
  <div class="login">

    <!--     Background Section -->
    <section>
     <video autoplay loop muted  style="width:100%" >

      <source src="./static/610941003.mp4" type="video/mp4">
      </video>

  <!--     <div >
      <vue-particles class="background" shapeType="edge" linesColor="#FF4136" color="#FF4136"></vue-particles>
    </div> -->
    </section>

    <section>
      <div class="header_menu">
       <Row type="flex" justify="end" >
        <Col span="1">
          <Button size="large"  @click="createAccountForm = true" type="text">注册</Button>

        </Col>
        <Col span="2">
         <Button size="large"  type="text">预留按钮</Button>
       </Col>
     </Row>

   </div>

 </section>

 <!--     sign in Section -->
 <section>

  <div >
    <Modal
    width="600"
    v-model="createAccountForm"
    @on-ok="createAccount"
    @on-cancel="cancel">
    <p slot="header" style="color:#FF4136;text-align:start; margin:10px; padding-top:10px;font-size: 30px;height:40px;">
      用户注册
    </p>
    <LoginForm ref="login_form"  @transferNewAccountInfo="setNewAccountInfo"></LoginForm>  

  </Modal>
</div>




</section>



<!--     Logo Section -->
<section>
  <transition appear name="zoom">
    <div>

      <h1> <icon style="color:#666;margin-top:6px;margin-left:20px;" name="logo1" scale="12"></icon>{{ logo_title }}</h1>

      <p class="welcome">{{ welcome }}</p>

    </div>

  </transition>

</section>


<!--     Login Section -->
<section class="login_form" >
  <transition appear name="fade">
    <Row type="flex" justify="center" >

      <Col span="4">
        <Form ref="loginForm" :model="loginForm" :rules="loginRule">
          <Form-item prop="username">
            <Input type="text" v-model="loginForm.username" placeholder="Username">
              <Icon type="person" slot="prepend"></Icon>
            </Input>
          </Form-item>
          <Form-item prop="password">
            <Input type="password" v-model="loginForm.password" placeholder="Password">
              <Icon type="locked" slot="prepend"></Icon>
            </Input>
          </Form-item>
          <Form-item>
            <Button  type="ghost" shape="circle"   @click="userLogin('loginForm')">登 录</Button>
          </Form-item>
        </Form></Col>

      </Row>
    </transition>


    <!--     Copyright Section -->
    <transition appear name="fade">
      <Row type="flex" justify="center">
        <p>
          Copyright &copy; 2017 LEISURE BOOKSTORE
        </p>
      </Row>
    </Row>
  </transition>
</section>


</div>
</template>

<script>
  import LoginForm from "../forms/LoginForm"
  export default {
    name: 'hello',
    data () {
      return {
        logo_title: 'Leisure',
        welcome: '欢迎来到Leisure线上书店',
        newAccountInfo:{},
        createAccountForm: false,
        loginForm: {
          username: '',
          password: ''
        },
        loginRule: {
          user: [
          // FIXME required: TRUE
          { required: true, message: '请填写用户名', trigger: 'blur' }
          ],
          password: [
          { required: true, message: '请填写密码', trigger: 'blur' },
        
          ]
        }
      }
    },
    methods: {

      //根据注册表单，更新新用户的用户信息
      setNewAccountInfo(msg) {
        this.newAccountInfo = msg;
      },

      createAccount() {

        
        //显示加载进度
        this.$Loading.start();
        if (!this.newAccountInfo.username) {
          this.$Loading.error();
          this.$Message.error('注册失败');
          return false;
        }

        //调用API创建用户
        this.$request.post('/api/user', {
          "username": this.newAccountInfo.username,
          "password": this.newAccountInfo.password
        })
        .then((response) => {

          //获取响应的state
          let state = response.data.state;
          if (state) {
            this.$Message.success("注册成功");
            this.$Loading.finish();
          }
          else {
            this.$Message.error("注册失败")
            this.$Message.error(response.data.info,5);
            this.$Loading.error();
          }

        }).catch((error) => {
          console.log(error);
          this.$Message.error(error);
        });

        //清空注册表单
        this.$refs.login_form.$refs.form.resetFields();

      },

          //注册取消
          cancel() {
            this.$refs.login_form.$refs.form.resetFields();
            this.$Message.info("取消注册")
          },

          //用户登录函数
          userLogin(name) {
            this.$refs[name].validate((valid) => {
              if (valid) {
                this.$Loading.start();
                this.$request.patch('/api/user?username='+this.loginForm.username+"&token="+this.$Crypto.MD5(this.loginForm.password))
                .then((response) => {

                  let state = response.data.state;
                  if (state) {
                    this.$Message.success("登录成功");
                    this.$Loading.finish();

                    this.$store.dispatch({
                      type: 'SET_USER_INFO',
                      username: this.loginForm.username,
                      password: this.loginForm.password
                    });

                    
                    this.$store.dispatch({
                      type: 'SET_USER_ID',
                      user_id: response.data.info.user_id
                    });

                    this.$ls.set('userid', response.data.info.user_id);
                    this.$ls.set('username', this.loginForm.username);
                    this.$ls.set('userlevel', response.data.info.userLevel);


                    //获取热门书籍
                    this.$store.dispatch('FETCH_POPULAR_BOOKS');
                    this.$router.push('/');
                  }
                  else {
                    this.$Message.success("登录失败 Error: "+response.data.info);
                    this.$Loading.error();
                    this.$refs[name].resetFields();
                  }

                }).catch((error) => {
                  console.log(error);
                  this.$Loading.error();
                  this.$Message.error('服务器繁忙');
                  this.$refs[name].resetFields();
                });
                

          } else {
            this.$Loading.error();
            this.$Message.error('请输入用户名和密码!');
          }
        })
          }
        },
        components:{
          "LoginForm": LoginForm,
        }
      }
    </script>

    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style scoped>
      h1 {
        margin-top: 135px;
        font-family: "Vladimir Script";
        font-weight: normal;
        font-size: 130px;
        color: #eeeeee;
      }

      p {
        margin-top: 40px;
        color: #bbbbbb;
        margin-bottom: 10px;
      }

      .welcome {
        margin-top: 0px;
        font-size: 15px;
      }

      video {
        position: fixed;
        right:0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        height: auto;
        overflow:hidden;
        width: auto;
        z-index: -99999;
        -webkit-filter:brightness(.2);
      }

      .login_form {
        margin-top: 80px;

      }

      .header_menu {
        margin:30px;
      }

      .background {
        position: fixed;
        right:0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        height: auto;
        overflow:hidden;
        width: auto;


      } 
    </style>
