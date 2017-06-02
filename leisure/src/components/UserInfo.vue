<template>
    <div class="layout1">
            <div>
            <Row type="flex"  justify="start"  >
                <Col  span="4">
                    <p class="tabTitle">个人信息</p>

                </Col>

            </Row>
        </div>

         <div>
            <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=3); margin-bottom:20px;"> 
        </div>



        <div>

         <Row  type="flex"  justify="center"  style="margin-bottom:20px;">
            <Col offset="2" span="6" >
                <Affix :offset-top="100">
                    <div class="rightMenu">

                        <!-- 我的钱包 -->
                        <div class="wallet" >
                            <Card style="width:100%">
                                <p slot="title" style="font-size:20px;font-weight:normal;color:#666;text-align:start">
                                    <Icon type="card"></Icon>
                                    我的信息
                                </p>

                                <p style="text-align:start;margin-left:20px;">用户名:</p>
                                <p style="margin-top:20px;"><span style="color:#303030;font-size:40px;">{{username}}</span></p>
                                <p style="text-align:start;margin-left:20px;">用户类型:</p>
                                <p v-if="userLevel" style="margin-top:20px;"><span style="color:#303030;font-size:40px;">管理员</span></p>
                                <p v-if="!userLevel" style="margin-top:20px;"><span style="color:#303030;font-size:40px;">普通用户</span></p>
                            </Card>

                        </div>


                        <!--    结算 -->
                        <div>

                        </div>

                    </div>
                </Affix>

            </Col>

            <Col offset="2" span="6" >
                <Affix :offset-top="100">
                    <div class="rightMenu">

                        <!-- 我的钱包 -->
                        <div class="wallet" >
                            <Card style="width:100%">
                                <p slot="title" style="font-size:20px;font-weight:normal;color:#666;text-align:start">
                                    <Icon type="card"></Icon>
                                    我的钱包
                                </p>

                                <p style="text-align:start;margin-left:20px;">当前余额</p>
                                <p style="margin-top:20px;">￥ <span style="color:#FF4136;font-size:40px;">{{animatedtotalBalance}}</span></p>


                                <Button type="ghost" style="margin-top:30px;" @click="topUpModal = true"  long>充值</Button>
                                <Button type="ghost" style="margin-top:20px" @click="withdrawModal = true" long>提现</Button>

                            </Card>

                        </div>


                        <!--    结算 -->
                        <div>

                        </div>

                    </div>
                </Affix>

            </Col>



        </Row>


    </div>









        <div >
            <Modal
            width="600"
            v-model="topUpModal"
            @on-ok="topupBalance"
            @on-cancel="cancel">
            <p slot="header" style="color:#FF4136;text-align:start; margin:10px; padding-top:10px;font-size: 30px;height:40px;">
                充值
            </p>
            <TopUpForm  ref="topup_form"  @transferAmount="transferNewAmount"></TopUpForm>

            </Modal>
        </div>

    <div >
        <Modal
        width="600"
        v-model="withdrawModal"
        @on-ok="withdrawBalance"
        @on-cancel="cancel">
        <p slot="header" style="color:#FF4136;text-align:start; margin:10px; padding-top:10px;font-size: 30px;height:40px;">
            提现
        </p>
        <WithdrawForm  ref="withdraw_form"  @transferAmount="transferNewAmount"></WithdrawForm>
        </Modal>
    </div>
   
    </div>
</template>

<script>
    import TopUpForm from "../forms/BalanceForm"
    import  WithdrawForm from "../forms/BalanceForm"
    import Avatar from 'vue-avatar/dist/Avatar'
    var TWEEN = require('tween.js');
    export default {
        data () {
            return {

                logoTitle: "Leisure",
                show: true,
                value2: 0,
                
                username: "",
                userId:0,
                userLevel:0,


                balance: 0,
                topUpModal: false,
                withdrawModal: false,
                animatedtotalBalance:0,
            }

        },
        components: {
            "TopUpForm": TopUpForm,
          "WithdrawForm": WithdrawForm,
        },
        watch: {
            balance (newValue, oldValue) {
              var vm = this
              function animate (time) {
                requestAnimationFrame(animate)
                TWEEN.update(time)
            }
            new TWEEN.Tween({ tweeningNumber: oldValue })
            .easing(TWEEN.Easing.Quadratic.Out)
            .to({ tweeningNumber: newValue }, 500)
            .onUpdate(function () {
              vm.animatedtotalBalance = this.tweeningNumber.toFixed(2)
          })
            .start()
            animate()
        }},
        mounted() {
            this.username = this.$ls.get('username', "null");
            this.userLevel = this.$ls.get('userlevel', "null");


            this.$request.get('/api/balance?id='+this.$ls.get('userid', 0))
            .then((response) => {
              let state = response.data.state;
              if (state) {


                this.balance = response.data.info.balance;

            }
            else {
                this.$Message.error("获取余额失败. Info:" + response.data.info);
                this.balance = 0;
                this.$Loading.error();
            }

              }).catch((error) => {
                 console.log(error);
                 this.$Message.error("获取余额失败. 服务器繁忙 Info:" + response.data.info);
             }); 
        },
        methods: {
            checkUser() {
                if(this.$ls.get('userid', 0) == 0) {
                    this.$router.push('/login');
                }
            },
            transferNewAmount (form) {
                this.newAmount = form.amount;
            },
            topupBalance() {
                this.checkUser();
                this.$Loading.start();
                this.$request.post('/api/balance', {user_id:this.$ls.get('userid', 0),amount:this.newAmount})
                .then((response) => {
                  let state = response.data.state;
                  if (state) {
                    this.$Message.success("充值" + this.newAmount + "成功");
                    this.balance = response.data.info.balance;


                    this.$Loading.finish();

                }
                else {
                    this.$Message.error("充值失败. Info:" + response.data.info);
                    this.$Loading.error();
                }

            }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                this.$Message.error("充值失败. 服务器繁忙 Info:" + response.data.info);

            }); 

        },
        withdrawBalance() {
            this.checkUser();
            this.$Loading.start();
            this.$request.put('/api/balance', {user_id:this.$ls.get('userid', 0),amount:this.newAmount})
            .then((response) => {
              let state = response.data.state;
              if (state) {
                this.$Message.success("支付" + this.newAmount + "成功");
                this.balance = response.data.info.balance;

                this.$Loading.finish();

            }
            else {
                this.$Message.error("支付失败. Info:" + response.data.info);
                this.$Loading.error();
            }

        }).catch((error) => {
            console.log(error);
            this.$Loading.error();
            this.$Message.error("通信失败. 服务器繁忙 Info:" + response.data.info);

        }); 

        },
        cancel() {
            this.$refs.topup_form.$refs.form.resetFields();
            this.$refs.withdraw_form.$refs.form.resetFields();
            this.$Message.info("取消充值")
        }

        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    .tabTitle {
        font-size: 30px;
        margin: 25px;
        color: #FF4136;
        margin-bottom:20px;

    }

    .userInfo {
        border-radius: 2px;
         transition: all 0.3s;
         border: 1px solid #d7dde4;
        
    }
    .userInfo:hover {
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    }

</style>