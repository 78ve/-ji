<template>
    <div class="cart">

        <Row type="flex"  align="bottom" >
            <Col  span="4">
                <p class="tabTitle">我的购物车</p>

            </Col>

        </Row>
        <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=3)"> 

        <div class="cartAndMenu">
            <Row type="flex"  justify="center" style="margin-bottom:10px">
                <Col  span="16">
                    <div  >

                        <!--   上栏，显示列表标题 -->
                        <Row  type="flex"  justify="center">
                            <Col  span="24">
                                <Row :gutter="2"  class="bookContainer" type="flex" justify="start" >

                                    <Col  class="vertical"  span="2" >
                                        <Checkbox
                                        :indeterminate="indeterminate"
                                        :value="checkAll"
                                        @click.prevent.native="handleCheckAll"
                                        ></Checkbox>
                                        <p  class="tableColumn">全选</p>
                                    </Col>
                                    <Col class="vertical" span="3"  >
                                        <p class="tableColumn" >书籍封面</p>
                                    </Col>

                                    <Col  :offset="1" class="vertical" span="4" >
                                        <p  class="tableColumn">名称</p>
                                    </Col>
                                    <Col :offset="2" class="vertical"  span="2" >
                                        <p  class="tableColumn">单价(元)</p>
                                    </Col> 
                                    <Col :offset="1" class="vertical"  span="2" >
                                        <p  class="tableColumn">数量</p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="2" >
                                        <p  class="tableColumn">金额(元)</p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="3" >
                                        <p class="tableColumn">操作</p>

                                    </Col>
                                </Row>

                            </Col>
                        </Row>


                        <!--   下栏，显示购物车中的物品 -->

                        <Row type="flex"  justify="center" >
                            <Col  span="24">

                                <transition-group name="list-complete">
                                    <div class="list-complete-item" v-if="hasCart" style="width:100%;"  v-for="book in booksInCart" :key="book">
                                        <Row   :gutter="2"  class="bookContainer cartBook" type="flex" justify="start"  >

                                            <Col  class="vertical"  span="2" >
                                                <Checkbox  @on-change="handleCheckSingle(book.id)"   :value="book.selected" ></Checkbox>
                                            </Col>
                                            <Col class="vertical" span="3"  >
                                                <div>
                                                    <img class="bookCover" :src="book.cover">

                                                </div>
                                            </Col>

                                            <Col  :offset="1" class="vertical" span="4" >
                                                <div class="vertical">
                                                    <div class="bookTitle">
                                                        <p style=";font-size:12px;">{{book.name}}</p>

                                                    </div>

                                                </div>

                                            </Col>
                                            <Col :offset="2" class="vertical"  span="2" >
                                                <div class="vertical">
                                                    <p style="font-size:14px;color:#999">￥{{book.price}}</p>
                                                </div>

                                            </Col> 
                                            <Col :offset="1" class="vertical"  span="2" >
                                                <div class="vertical" >
                                                    <Input-number style="font-size:14px;" :max="10" :min="1" v-model="book.quantity"></Input-number>
                                                </div>

                                            </Col>
                                            <Col :offset="1" class="vertical"  span="2" >
                                                <div class="vertical" >
                                                    ￥ <p style="font-size:14px;color:#FF4136">{{Math.round((book.price * book.quantity)*100)/100}}</p>
                                                </div>

                                            </Col>
                                            <Col :offset="1" class="vertical"  span="3" >
                                                <div class="vertical">
                                                    <Button-group style=""  shape="circle">

                                                        <Button type="ghost" @click="removeBook(book.id)">
                                                            <Icon type="close" ></Icon>
                                                        </Button>
                                                    </Button-group>
                                                </div>

                                            </Col>
                                        </Row>
                                    </div>
                                </transition-group>

                            </Col>
                        </Row>

                        <transition name='fadeUp' mode="out-in">
                            <Row v-if="(! isLoading & ! hasCart)" type="flex"  justify="center" style="width:100%;height:600px;" >
                              <Col class="vertical"   span="4" >

                                <div>
                                <icon style="color:#666;margin-left:300px;" name="lookmyeye" scale="20"></icon>
                                </div>


                            </Col>
                            <Col class="vertical" span="20">

                                <div>
                                    <p><span style="font-size:80px;color:#bbb;">空空如也</span></p>
                                </div>


                            </Col>

                            </Row>

                        </transition>
                        <transition name='fadeUp' mode="out-in">
                            <Row v-if="isLoading" type="flex"  justify="center" style="width:100%;height:600px;" >
                                <Col class="vertical" style="margin-top:100px;"  span="12">

                                    <div>

                                        <Spin size="large"></Spin>

                                    </div>


                                </Col>

                            </Row>

                        </transition>

                    </div>
                </Col>



                <!--         右侧菜单 -->
                <Col span="6" >
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

                            <!--  金额计算 -->
                            <div class="pay">
                                <Card style="width:100%">

                                    <p style="margin-top:20px;">总计：
                                        <span style="color:#FF4136;font-size:50px;">{{animatedtotalMoney}}
                                        </span>元
                                    </p>


                                    <Button type="primary" circle style="margin-top:30px;" :loading="generateOrderLoading" @click="generateOrder" long>结算</Button>

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
  var TWEEN = require('tween.js');
  export default {
    data () {
      return {
        self:this,
        show: true,
        hasCart:false,

        topUpModal: false,
        withdrawModal: false,

        balance: 0,
        username:"",

        booksInCart:[],

        isLoading:true,
        indeterminate: false,
        checkAll: true,

        money:0,

        animatedtotalMoney:0,

        generateOrderLoading: false,

        animatedtotalBalance:0,



        newAmount: 0
    }

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
    },
    totalMoney (newValue, oldValue) {
      var vm = this
      function animate (time) {
        requestAnimationFrame(animate)
        TWEEN.update(time)
      }
      new TWEEN.Tween({ tweeningNumber: oldValue })
        .easing(TWEEN.Easing.Quadratic.Out)
        .to({ tweeningNumber: newValue }, 500)
        .onUpdate(function () {
          vm.animatedtotalMoney = this.tweeningNumber.toFixed(2)
        })
        .start()
      animate()
    }
  }
,
components:{
          "TopUpForm": TopUpForm,
          "WithdrawForm": WithdrawForm,
        },
computed: {
    totalMoney() {
        let money = 0;
        for(let a=0;a<this.booksInCart.length;a++){
            if (this.booksInCart[a].selected) {
                money += this.booksInCart[a].price * this.booksInCart[a].quantity;
            }
        }
        return money;
    },
    bookList() {
        let list = [];
        for(let a=0;a<this.booksInCart.length;a++){
            if (this.booksInCart[a].selected) {
                list.push(this.booksInCart[a].book_id);
            }
        }
        return list
    }
},
mounted() {
    console.log("已经挂载");
    this.hasCart = false;
    this.$Loading.start();
    this.$request.get('/api/cart?id='+this.$ls.get('userid', 0))
    .then((response) => {
      let state = response.data.state;
      if (state) {
        this.$Message.success("获取购物车信息成功");

        this.$Loading.finish();
        this.isLoading = false;
        this.hasCart = true;

        this.booksInCart = response.data.info.reverse();
        
        let money = 0;
        for(let a=0;a<this.booksInCart.length;a++){
            if (this.booksInCart[a].selected) {
                money += this.booksInCart[a].price * this.booksInCart[a].quantity;
            }
        }
        this.animatedtotalMoney = money;




    }
    else {
        this.$Message.warning("购物车为空");
        this.$Loading.finish();
        this.isLoading = false;

        this.hasCart = false;

    }

    }).catch((error) => {
        console.log(error);
        this.$Loading.error();
        this.hasCart = false;
        this.isLoading = false;
        this.$Message.error('服务器繁忙');

    }); 


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
    generateOrder () {
        this.checkUser();
        this.generateOrderLoading = true;
        this.$Loading.start();
        if (this.booksInCart.length == 0) {
            this.$Loading.error();
            this.generateOrderLoading = false;
            this.$Message.error("购物车为空");
            return;
        }
        this.$request.post('/api/order',{
            user_id:this.$ls.get('userid', 0),
            pay_amount:this.totalMoney,
            book_list:this.bookList,
            status:1
        })
        .then((response) => {
            let state = response.data.state;
            if (state) {
                this.$Message.success("生成订单成功, 请前往订单页面进行支付", 5);

                this.generateOrderLoading = false;
                
                let book=0;
                for ( book in this.booksInCart)  {
                    if (this.booksInCart[book].selected) {
                        this.$request.delete('/api/cart?id='+this.booksInCart[book].id)
                        .then((response) => {
                            let state = response.data.state;
                            if (state) {
  
                            }
                            else {
                                this.$Message.error(response.data.info);
                            }

                        }).catch((error) => {
                            console.log(error);
                            this.$Loading.error();
                            this.$Message.error('服务器繁忙');

                        }); 
                    }
                }
                for(let a=0;a<this.booksInCart.length;a++){
                    if (this.booksInCart[a].selected) {
                        
                        this.booksInCart.splice(a,1);
                        a=a-1;
                    }
                }
                this.$Loading.finish();

            }
            else {
                this.$Message.warning("生成订单失败");
                this.$Loading.finish();

            }

        }).catch((error) => {
            console.log(error);
            this.$Loading.error();

            this.$Message.error('服务器繁忙');

        }); 

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
        this.$Message.info("取消注册")
    },
    handleCheckSingle() {
        this.$Message.success(arguments[0]);
        this.checkAll = false;

        for(let a=0;a<this.booksInCart.length;a++){
            if (this.booksInCart[a].id == arguments[0]) {
                this.booksInCart[a].selected = ! this.booksInCart[a].selected;
            }
        } 

        
    },
    changeNumber() {
        this.$Message.success(arguments);
        
    },
    removeBook() {
        this.checkUser();
        // console.log(this.booksInCart);
        this.$Loading.start();
        this.$request.delete('/api/cart?id='+arguments[0])
        .then((response) => {
          let state = response.data.state;
          if (state) {
            this.$Message.success("从购物车移除了书籍《"+this.booksInCart[0].name+"》");

            this.$Loading.finish();
            this.hasCart = true;

            for(let a=0;a<this.booksInCart.length;a++){
                if (this.booksInCart[a].id == arguments[0]) {
                    this.booksInCart.splice(a,1);
                }
            }


            if (this.booksInCart.length == 0) {
                this.hasCart = false;
            }


        }
        else {
            this.$Message.error("移除书籍失败. Info:" + response.data.info);
            this.$Loading.error();

        }

        }).catch((error) => {
            console.log(error);
            this.$Loading.error();
            this.hasCart = false;
            this.$Message.error('服务器繁忙');

        }); 
    
    },
    mockData () {
        let data = [];
        for (let i = 0; i < 4; i++) {
            data.push({
                id:i + 2,
                book_id: i+1,
                selected: true,
                name: '特别敢，又特别美',
                cover: "http://oqnxnowx3.bkt.clouddn.com/test.jpg",
                quantity:Math.floor(Math.random () * 3 + 1),
                price:Math.floor(Math.random () * 100 + 1)
            })
        };
        return data;
    },
    handleCheckAll () {
                if (this.indeterminate) {
                    this.checkAll = false;
                } else {
                    this.checkAll = !this.checkAll;
                }
                this.indeterminate = false;

                if (this.checkAll) {
                    for(let a=0;a<this.booksInCart.length;a++){
                        if (! this.booksInCart[a].selected) {
                            this.booksInCart[a].selected = true;
                        }
                    }
                } else {
                    for(let a=0;a<this.booksInCart.length;a++){
                        if (this.booksInCart[a].selected) {
                            this.booksInCart[a].selected = false;
                        }
                    }
                }
            }
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .layout1{
        position: relative;
        text-align:center;
        border-radius: 4px;

        white-space: nowrap;

        min-height: 700px;
    }
    .cart {

        width: 90%;
        margin:0 auto;
        /*margin-top: 20px;*/


    }

    .wallet {
        margin:20px;
        margin-top: 0px;

    }

    .cartAndMenu {
        margin-top: 20px;
    }

    .rightMenu {
        min-height: 400px;

    }

    .bookCover {
        width: 70%;
        border-radius: 2px;
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    }

    img {
        width: 100px;
        margin:5px;
    }

    .bookContainer {
        margin-bottom: 10px;
        transition:all .3s ease-in-out;
    }

    .bookContainer:hover {

      /*  margin-top: -1px;*/
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
        transition:all .3s ease-in-out;


    }

    .tabTitle {

        margin: 25px;
        color: #FF4136;
        font-size: 30px;

    }


    .vertical{
        display: flex;
        justify-content: center;
        align-items:center;
        display:-webkit-flex;
    }

    .tableColumn {
        font-size: 12px;
        color: #999
    }

    .bookTitle {

        font-size: 12px;
        transition:all .3s ease-in-out;
        overflow:hidden; 

        white-space:normal; 
        width:10em; 
    }

    .cartBook {
        border: 1px solid #d7dde4;
        width: 100%;
        height: auto;
    }

    .pay {
        margin:20px;
    }

    .list-complete-item {
        transition: all 1s;
        display: inline-block;
        margin-right: 10px;
    }
    .list-complete-enter, .list-complete-leave-active {
        opacity: 0;
        transform: translateX(30px);
    }
    .list-complete-leave-active {
        position: absolute;
    }




</style>