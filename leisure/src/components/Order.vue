<template>
    <div class="order">
        <Row type="flex"  align="bottom" >
            <Col  span="4">
                <p class="tabTitle">我的订单</p>

            </Col>

        </Row>
        <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=3)"> 


        <div class="orderHeader" style="min-height: 400px;">


            <!--   显示表格标题 -->

            <Row  type="flex"  justify="center" class="orderTitle">
                <Col  span="20">

                    <Row :gutter="2"  type="flex" justify="start"  >
                        <Col  class="vertical"  span="2" >
                            <Checkbox
                            :indeterminate="indeterminate"
                            :value="checkAll"
                            @click.prevent.native="handleCheckAll"
                            ></Checkbox>
                            <p  class="tableColumn">全选</p>
                        </Col>
                        <Col class="vertical" span="5" >
                            <p class="tableColumn" >商品信息</p>
                        </Col>

                        <Col  :offset="1"  class="vertical" span="3" >
                            <p  class="tableColumn">实付款</p>
                        </Col>
                        <Col :offset="1" class="vertical"  span="3" >
                            <p  class="tableColumn">生成日期</p>
                        </Col> 
                        <Col :offset="1" class="vertical"  span="3" >
                            <p  class="tableColumn">订单状态</p>
                        </Col>
                        <Col :offset="1" class="vertical"  span="4" >
                            <p  class="tableColumn">操作</p>
<!--                             <Button-group style="" size="large"  shape="circle">
                                            <Button type="primary" @click="payMultiOrder">
                                                支付
                                            </Button>
                                            <Button type="primary" @click="removeMultiOrder">
                                               移除
                                            </Button>
                                        </Button-group> -->

                        </Col>
                    </Row>

                </Col>
            </Row>

            <!-- 显示订单内容 -->

            <Row  type="flex"  justify="center">
                <Col  span="20">
                    <transition-group name="list-complete">
                        <div class="list-complete-item" v-if="hasOrder" style="width:100%;"  v-for="order in orders" :key="order">


                            <div class="orderItem" :class="{ active: order.status}">
                                <Row   type="flex" justify="start"  class="orderItemHeader"  >

                                    <Col    class="vertical" span="1" >
                                        <Checkbox  @on-change="handleCheckSingle(order.id)"  :value="order.selected" ></Checkbox>
                                    </Col>
                                    <Col  class="vertical"  span="1"  >
                                       <icon style="color:#666;" name="sad" scale="2"></icon>
                                    </Col> 
                                    <Col  class="vertical"  span="6"  >
                                        <p  class="tableColumn">订单号：{{order.serial_number}}</p>
                                    </Col>
                                </Row>

                                <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=0.5)"> 


                                <Row :gutter="2"  class="orderItemContent" type="flex" justify="start" >

                                    <Col class="vertical"  :offset='2' span="5"  >



                                        <Row class="orderCover"  type="flex"  justify="center">
                                            <Col class="vertical" v-for="cover in order.cover_list" :key="order"  :span="24/order.cover_list.length" style="margin-top:5px;">

                                                <img class="bookCover" :src="cover">

                                            </Col>
                                        </Row>





                                    </Col>

                                    <Col  :offset="1"  class="vertical" span="3"  >
                                        <p style="font-size:14px;color:#999">￥ <span style="color:#FF4136">{{order.pay_amount}}</span></p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="3" >
                                        <p  class="tableColumn">{{order.created_at}}</p>
                                    </Col> 
                                    <Col :offset="1" class="vertical"  span="3" >
                                        <p v-if=" order.status == 1"  class="tableColumn">等待支付</p>
                                        <p v-if=" order.status == 2"  class="tableColumn">派送中</p>
                                        <p v-if=" order.status == 3"  class="tableColumn">已收货</p>
                                        <p v-if=" ! order.status "  class="tableColumn">完成交易</p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="4" >

                                        <Button-group style=""  shape="circle">
                                            <Button v-if=" order.status == 1 " type="ghost" @click="payOrder(order.id)">
                                                支付
                                            </Button>
                                            <Button v-if=" order.status == 2 " type="ghost" @click="confirmReceive(order.id)">
                                                确认收货
                                            </Button>
                                            <Button v-if=" order.status == 3 " type="ghost" @click="preCommentOrder(order.book_list)">
                                                评论
                                            </Button>
                                            <Button type="ghost" @click="removeOrder(order.id)">
                                               移除
                                            </Button>
                                        </Button-group>

                                    </Col>
                                </Row>

                            </div>

                        </div>
                    </transition-group>
                </Col>
            </Row>



            <transition name='fadeUp' mode="out-in">
                <Row v-if="(! isLoading & ! hasOrder)" type="flex"  justify="center" style="width:100%;height:600px;" >
                    <Col class="vertical"   span="4" >

                        <div>
                        <icon style="color:#666;margin-left:600px;" name="noface" scale="20"></icon>
                        </div>


                    </Col>
                    <Col class="vertical" span="20">

                        <div>
                            <p><span style="font-size:80px;color:#bbb;">暂无订单</span></p>
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


        <div >
            <Modal
            width="600"
            v-model="commentModal"
            @on-ok="commentOrder"
            @on-cancel="cancel">
            <p slot="header" style="color:#FF4136;text-align:start; margin:10px; padding-top:10px;font-size: 30px;height:40px;">
                填写评论
            </p>
            <CommentForm  ref="comment_form"  @transferComment="getComment"></CommentForm>

        </Modal>
    </div>



    </div>
</template>

<script>
    import CommentForm from "../forms/CommentForm"
    export default {
        data () {
            return {
                orders: [],
                hasOrder:false,
                indeterminate: false,
                checkAll: false,

                commentModal: false,
                isLoading:true,
                username:"",
                comment:"",
                rate:"",
                book_list:[]
            }

        },
        mounted() {

            console.log("已经挂载");
            this.hasCart = false;
            this.isLoading = true;
            this.$Loading.start();
            this.$request.get('/api/order?user_id='+this.$ls.get('userid', 0))
            .then((response) => {
                let state = response.data.state;
                if (state) {
                    this.$Message.success("获取订单信息成功");

                    this.$Loading.finish();
                    this.hasOrder = true;
                    this.isLoading = false;


                    this.orders = response.data.info.reverse().sort(this.sortOrder);

                }
                else {
                    this.$Message.warning("当前没有订单");
                    this.$Loading.finish();

                    this.hasOrder = false;
                    this.isLoading = false;

                }

            }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                this.hasOrder = false;
                this.isLoading = false;
                this.$Message.error('服务器繁忙');

            }); 
        },
        computed: {
            orderList() {
                let order_id_list = [];
                for(let a=0;a<this.orders.length;a++){
                    if (this.orders[a].selected) {
                        order_id_list.push(this.orders[a].id) 
                    }
                }
                return order_id_list;
            }
        },
        components:{
          "CommentForm": CommentForm
        },
        methods: {
            preCommentOrder() {
                this.book_list = arguments[0];
                this.commentModal = true;
            },
            getComment() {
                console.log(arguments[0]);


                this.comment = arguments[0].comment;
                this.rate = arguments[0].rate;
            },
            cancel() {
                this.$refs.comment_form.$refs.form.resetFields();
                this.$Message.info("取消评论");
            },
            checkUser() {
                if(this.$ls.get('userid', 0) == 0) {
                    this.$router.push('/login');
                }
            },
            sortOrder(a,b) {
                return b.status - a.status
            },
            commentOrder() {
                this.checkUser();
                this.$Loading.start();
                this.$request.post('/api/comment', {
                    user_id:this.$ls.get('userid', 0),
                    comment:this.comment,
                    book_list:this.book_list,
                    rate:this.rate})
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("评论订单成功");

                        let temp = this.orders;
                        this.orders = [];
                        this.orders = temp.sort(this.sortOrder);

                        this.$Loading.finish();
                        this.commentModal = false;

                    }
                    else {
                        this.$Message.warning("评论订单失败 Info:" + response.data.info);
                        this.$Loading.finish();
                        this.commentModal = false;
                    }
                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.commentModal = false;

                    this.$Message.error('服务器繁忙');
                });               
            },
            confirmReceive() {
                this.checkUser();
                this.$Loading.start();
                this.$request.put('/api/order', {
                    user_id:this.$ls.get('userid', 0),
                    order_id:arguments[0],
                    order_status:3})
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("更新订单状态成功");
                        this.$Loading.finish();
                        for(let a=0;a<this.orders.length;a++){
                            if (this.orders[a].id == arguments[0]) {
                                this.orders[a].status = 3;
                            }
                        }
                    }
                    else {
                        this.$Message.warning("更新订单状态失败");
                        this.$Loading.finish();
                    }
                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.$Message.error('服务器繁忙');
                });
            },
            payOrder() {
                this.checkUser();
                this.$Loading.start();
                this.$request.put('/api/order', {
                    user_id:this.$ls.get('userid', 0),
                    order_id:arguments[0],
                    order_status:2})
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("更新订单状态成功");

                        this.$Loading.finish();

                        for(let a=0;a<this.orders.length;a++){
                            if (this.orders[a].id == arguments[0]) {
                                this.orders[a].status = 2;
                            }
                        }
                    }
                    else {
                        this.$Message.warning("更新订单状态失败");
                        this.$Loading.finish();
                    }

                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();

                    this.$Message.error('服务器繁忙');
                });
            },
            removeOrder () {
                this.checkUser();
                this.$Loading.start();
                let list = [arguments[0]];
                this.$request.patch('/api/order', {order_id_list: list})
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("移除订单成功");
                        this.$Loading.finish();
                        for(let a=0;a<this.orders.length;a++){
                            if (this.orders[a].id == arguments[0]) {
                                this.orders.splice(a,1);
                            }
                        }
                        if (this.orders.length == 0) {
                            this.hasOrder = false;
                        }
                    }
                    else {
                        this.$Message.warning("移除订单失败, Info:" + response.data.info);
                        this.$Loading.finish();
                    }
                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.$Message.error('服务器繁忙');
                }); 

            },
            payMultiOrder() {
                for(let a=0;a<this.orders.length;a++){
                    if (this.orders[a].selected) {
                        this.orders[a].status = 1;
                    }
                }
            },
            removeMultiOrder() {
                this.checkUser();
                this.$Loading.start();
                this.$Message.info(this.orderList);

                let list = [];
                for(let a=0;a<this.orders.length;a++){
                    if (this.orders[a].selected) {
                        list.push(this.orders[a].id); 
                    }
                }
                this.$request.patch('/api/order', {order_id_list: list})
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("批量移除订单成功");
                        this.$Loading.finish();
                        for(let a=0;a<this.orders.length;a++){
                            if (this.orders[a].selected) {
                                a = a-1;
                            }
                        }
                        if (this.orders.length == 0) {
                            this.hasOrder = false;
                        }
                    }
                    else {
                        this.$Message.warning("批量移除订单失败, Info:" + response.data.info);
                        this.$Loading.finish();
                    }
                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.$Message.error('服务器繁忙');
                }); 
            },
            handleCheckSingle() {
                this.$Message.success(arguments[0]);
                this.checkAll = false;

                for(let a=0;a<this.orders.length;a++){
                    if (this.orders[a].id == arguments[0]) {
                        this.orders[a].selected = ! this.orders[a].selected;
                    }
                } 
            },
            handleCheckAll () {
                if (this.indeterminate) {
                    this.checkAll = false;
                } else {
                    this.checkAll = !this.checkAll;
                }
                this.indeterminate = false;

                if (this.checkAll) {
                    for(let a=0;a<this.orders.length;a++){
                        if (! this.orders[a].selected) {
                            this.orders[a].selected = true;
                        }
                    }
                } else {
                    for(let a=0;a<this.orders.length;a++){
                        if (this.orders[a].selected) {
                            this.orders[a].selected = false;
                        }
                    }
                }
            },
            mockData () {
                let data = [];
                for (let i = 0; i < 4; i++) {
                    data.push({
                        id:i + 2,
                        serial_number: 1111111111111,
                        selected: false,
                        created_at: '2017-05-31 18:50:53',
                        cover_list: ["http://oqnxnowx3.bkt.clouddn.com/test.jpg","http://oqp77idbc.bkt.clouddn.com/%E8%8B%B1%E8%AF%AD.png"],
                        status:0,
                        pay_amount:Math.floor(Math.random () * 100 + 1)
                    })
                };
                return data;ss
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .order{
        width: 90%;
        margin:0 auto;
    }

    .tabTitle {
        margin: 25px;
        color: #FF4136;
        font-size: 30px;
    }
    .orderHeader {
        margin-top: 20px;
    }

    .vertical{
        display: flex;
        justify-content: center;
        align-items:center;
        display:-webkit-flex;
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
    .orderItem {
        margin-bottom: 10px;
        transition:all .3s ease-in-out;
        border: 1px solid #d7dde4;
        filter:brightness(.7) grayscale(1) blur(1px);;
        background-color: #fff;
    }

    .orderItem:hover {
        /*margin-top: -1px;*/
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
        transition:all .3s ease-in-out;

    }
    .active {
        filter:brightness(1);
    }
    .orderTitle {
        margin-bottom: 20px;
    }
    .tableColumn {
        font-size: 12px;
        color: #999
    }
    .bookCover {
        width: 55%;
        max-width: 100px;
        max-height: 100px;
        border-radius: 2px;
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .20), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    }
    .orderItemHeader {
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .orderItemContent {
        margin-bottom: 8px;
    }
    .orderCover {
        
        height: 100px;
    }
</style>