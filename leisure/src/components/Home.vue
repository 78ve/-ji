<template>
   <div class="layout_home">

    <div v-if="showCarousel">
    <transition appear name="zoom">
        <div  class="home_display">
            <Carousel autoplay  arrow="never" dots="inside">
                <Carousel-item>
                    <div class="demo-carousel" style="background-color:#333">
                        <p style="color:#fff;font-size:80px;padding-top:70px;padding-left:550px;font-family:'Century Gothic'">
                            AD 1 
                        </p>


                    </div>
                </Carousel-item>
                <Carousel-item>
                    <div class="demo-carousel" style="background-color:#444">
                         <p style="color:#fff;font-size:80px;padding-top:70px;padding-left:550px;font-family:'Century Gothic'">
                            AD 2
                        </p>
                    </div>
                </Carousel-item>
                <Carousel-item>
                    <div class="demo-carousel" style="background-color:#555">
                         <p style="color:#fff;font-size:80px;padding-top:70px;padding-left:550px;font-family:'Century Gothic'">
                            AD 3
                        </p>
                    </div>
                </Carousel-item>
                <Carousel-item>
                    <div class="demo-carousel" style="background-color:#666">
                         <p style="color:#fff;font-size:80px;padding-top:70px;padding-left:550px;font-family:'Century Gothic'">
                            AD 4
                        </p>
                    </div>
                </Carousel-item>
            </Carousel>
        </div>
        </transition>
        
    </div>

    <div class="bookList" >
   
    <Row >
    
        <i-col span="4">

            <Menu @on-select="getBooks"  accordion theme="light" active-name="popular">

                <Poptip  trigger="hover" content="根据名称模糊搜索" placement="top-start">
                    <Input  style="width:200px; margin:20px;"  @on-enter="searchBook"  v-model="search" icon="ios-search" placeholder="书名、作者" ></Input>
                </Poptip>
                <Menu-group title="图书分类">
                </Menu-group>
                <Menu-item name="popular"><Icon type="fireball"></Icon>热门图书</Menu-item>
                <Menu-item name="newest"><Icon type="ionic"></Icon>最新首发</Menu-item>
                <Submenu name="1">
                    <template slot="title">
                        <Icon type="ios-book"></Icon>
                        文艺
                    </template>
                    <Menu-item name="novel">小说</Menu-item>
                    <Menu-item name="literature">文学</Menu-item>
                    <Menu-item name="art">艺术</Menu-item>
                    <Menu-item name="biography">传记</Menu-item>
                </Submenu>
                <Submenu name="2">
                    <template slot="title">
                        <Icon type="university"></Icon>
                        人文社科
                    </template>
                    <Menu-item name="philosophy">哲学</Menu-item>
                    <Menu-item name="history">历史</Menu-item>
                    <Menu-item name="politics">政治</Menu-item>
                    <Menu-item name="culture">文化</Menu-item>
                </Submenu>
                <Submenu name="3">
                    <template slot="title">
                        <Icon type="cube"></Icon>
                        科技
                    </template>
                    <Menu-item name="computer">计算机</Menu-item>
                    <Menu-item name="industry">工业技术</Menu-item>
                    <Menu-item name="medicine">医学</Menu-item>
                    <Menu-item name="science">自然科学</Menu-item>
                </Submenu>
                <Submenu name="4">
                    <template slot="title">
                        <Icon type="lightbulb"></Icon>
                        期刊杂志
                    </template>
                    <Menu-item name="tourism">旅游</Menu-item>
                    <Menu-item name="fashion">时尚</Menu-item>
                    <Menu-item name="journey">专业期刊</Menu-item>
                    <Menu-item name="education">教育科普</Menu-item>
                </Submenu>
                <Submenu name="5">
                    <template slot="title">
                        <Icon type="ios-paper"></Icon>
                        漫画
                    </template>
                    <Menu-item name="hinata">同人</Menu-item>
                    <Menu-item name="action">动作</Menu-item>
                    <Menu-item name="behold">猎奇</Menu-item>
                    <Menu-item name="fantasy">奇幻</Menu-item>
                </Submenu>
                <Submenu name="6">
                    <template slot="title">
                        <Icon type="leaf"></Icon>
                        儿童读物
                    </template>
                    <Menu-item name="enlish">少儿英语</Menu-item>
                    <Menu-item name="quiz">成长益智</Menu-item>
                    <Menu-item name="tales">儿童文学</Menu-item>
                    <Menu-item name="enlightened">启蒙读物</Menu-item>
                </Submenu>
            </Menu>

        </i-col> 


        <i-col span="19">
            <div class="content"  >
            <div>

             <Row type="flex"   >
             <Col class="vertical"   span="10">
                 <p>{{resultTitle}}</p>

             </Col>
             <Col class="vertical" span="8" >
             <div>
                        <Spin v-if="bookLoading"   size="large" >
                    
                </Spin>
             </div>
                  
             </Col>
                <Col class="vertical" span="2" style="margin-top:200x" offset="4">
                     <Poptip trigger="hover" title="" content="显示书籍简要介绍">
            
                        <i-switch v-model="showBriefIntro" @on-change="showBrief" size="large">
                               <span style="font-size:10px" slot="open">ON</span>
                               <span style="font-size:10px" slot="close">OFF</span>

                        </i-switch>
                    </Poptip>
               
                </Col>
            </Row>

                
                
                <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=3)"> 

            </div>
               
                <div class="bookscontent"   >
                        <Page v-if="hasBook" style="margin-left:900px;margin-top:20px;" :current="pageNumber" :total="resultsTotal" :page-size="pageSize" @on-change="changePages" simple></Page>
                     <transition-group
                    mode="out-in"
                    name="fadeUp">
                    <div v-if="hasBook" style="padding-top:0px;margin-top:0px;"  v-for="booksinfo in showBooks" :key="booksinfo">
                    <book  @transferSelectBookInfo="enterBookDetails" :show-brief-intro="showBriefIntro" :books-info="booksinfo" >
                      </book>

                  </div>


                 </transition-group>
                 <Page v-if="hasBook" style="margin-left:900px;margin-top:20px;" :current="pageNumber" :total="resultsTotal" :page-size="pageSize" @on-change="changePages" simple></Page>

                 <transition
                   mode="out-in"
                    name="zoom">
                    <div v-if="noBook" style="text-align:center;margin-top:220px;" >
                        <span style="font-size:100px;color:#bbb;">无图书</span>
                  </div>
                 </transition>

              <!--   <Spin v-if="bookLoading"   size="large" style="z-index:10;margin-top:280px;margin-left:500px;">
                    
                </Spin> -->
              </div>

          </div>


      </i-col>
  </Row>



  <div>
    <Modal v-model="bookDetailsModal" width="900"  :styles="{top: '20px'}">
        <p slot="header" style="color:#FF4136;text-align:start; margin:10px; padding-top:10px;font-size: 30px;height:0px;">
          <!--   书籍详情 -->
        </p>
        <div>

                 <div>   
                <Row align="top" >
                <Col span="10">
                    <div > 
                        <img class="bookCover" :src="bookDetails.cover">
                    </div>
                </Col>
                    
                    <Col span="14" ><div> 
                    <p style="text-align:start;color:#333333;font-size:25px;margin-bottom:5px;">{{bookDetails.name}}</p>
                    <p style="text-align:start;color:#999999;font-size:15px;margin-top:0px;">{{bookDetails.briefInfo}}</p>
                    <p style="text-align:start;color:#666666;font-size:15px;margin-bottom:20px;">

                    作者：<span style="color:#FF4136;">{{bookDetails.author}}</span></p>
                    <p style="text-align:start;color:#666666;font-size:12px;margin-bottom:5px;margin-top:10px;">

                    出版社：{{bookDetails.publisher}}</p>

                    <p style="text-align:start;color:#666666;font-size:12px;margin-bottom:5px;margin-top:10px;">

                    出版日期：{{bookDetails.publishDate}}</p>
                    <p style="text-align:start;color:#666666;font-size:12px;margin-bottom:5px;margin-top:10px;">

                    包装：{{bookDetails.packaging}}</p>
                    <p style="text-align:start;color:#666666;font-size:12px;margin-bottom:5px;margin-top:10px;">

                    页数：{{bookDetails.pagesNumber}}</p>
                    <p style="text-align:start;color:#666666;font-size:12px;margin-bottom:40px;margin-top:10px;">

                    国际标准书号ISBN：{{bookDetails.ISBN}}</p>

                     <p style="text-align:start;color:#666666;font-size:20px;margin-bottom:10px;margin-top:10px;">

                    <span>￥ </span><span style="color:#FF4136;font-size:30px;">{{bookDetails.price}}</span></p>



                    <!-- <Rate disabled show-text  style="margin:25px;margin-top:0px" v-model="bookDetails.rate">
                         <span style="color: #f5a623">{{ bookDetails.rateNumber }}</span>人评分
                    </Rate> -->

                    <div>   
                        <Tooltip content="输入购买数量" placement="top">
                        <Input-number style="margin-left:25px" :max="10" :min="1" v-model="orderBookNumber"></Input-number>
                        </Tooltip>

                        <Button  type="ghost" style="margin-left:100px" size="large" :loading="addIntoCartLoading" @click="addIntoCart(bookDetails)">加入购物车</Button>
                        <Button type="primary" style="margin-left:25px" size="large" :loading="generateOrderLoading"  @click="generateOrder(bookDetails)">立即购买</Button>
                    </div>
                    

                 </div></Col>
            </Row>
            </div>


            <div  style="margin-left:20px;margin-right:20px;">   

                <Tabs value="name1">
                    <Tab-pane   label="书籍详情" name="name2">

                    

                    <Row type="flex" justify="center" >
                        
                        <Col class="vertical shadow"  span="23" >
                             
                            <img class="bookDetails"  :src="bookDetails.details">
                                 
                        </Col>
                    </Row>

                       

                    </Tab-pane>
                    <Tab-pane @on-click="showComments"  label="评论" name="name3">

                        <div>

                        <Row    type="flex" justify="center" >

                            <Col   span="22" >
                                <transition-group name="list-complete">
                                    <div  class="list-complete-item commentItemWrapper" style="width:100%;"  v-for="comment in comments" :key="comment">


                                        <div class="commentItem" >

                                            <Row   type="flex" justify="start"   class="commentItemHeader"  >
                                                <Col  class="vertical"  span="24"  >
                                                    <p  class="tableColumn">日期：{{comment.created_at}}</p>
                                                </Col>
                                            </Row>
                                            <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=0.5)"> 
                                            <Row :gutter="2"  class="commentItemContent" type="flex" justify="start" >

                                            

                                                <Col  :offset="1"  class="vertical" span="4"   >
                                                <avatar :username="comment.username"
                                                    class="avatar"
                                                    background-color="#FFC107"
                                                    :size="40"></avatar> <p class="commentUsername">{{comment.username}}</p>
                                                </Col>
                                                 <Col :offset="1" class="vertical"  span="18"  >
                                                    <p  class="comment">{{comment.content}}</p>
                                                </Col> 
                                            </Row>

                                        </div>

                                    </div>
                                </transition-group>
                            </Col>
                        </Row>
                    </div>


                    </Tab-pane>
                </Tabs>

            </div>
            
            

            </div>
            <div slot="footer">
                
            </div>
        </Modal>

    </div>


</div>
</div>
</template>

<script>
    import Avatar from 'vue-avatar/dist/Avatar'
    import MugenScroll from 'vue-mugen-scroll'
    import BookCard from './BookCard';
    export default {
        data () {
            return {
                userLevel: 3,
                logoTitle: "Melody",
                show: true,

                bookLoading:true,
                hasBook:true,
                noBook:false,

                username:"",

                addIntoCartLoading: false,
                generateOrderLoading: false,

                pageSize:16,

                showCarousel:true,
                pageNumber:1,
                resultsTotal:0,

                hasComment: false,
                isCommentLoading: true,

                //显示书籍简要介绍
                showBriefIntro: false,

                // 书籍详情
                bookDetailsModal: false,
                bookDetails:{},

                booksType: 'popular',

                busy: false,


                comments:[],



                //购买书籍
                orderBookNumber:1,


                //搜索
                search:"",

                //书籍列表标题
                resultTitle:"热门图书",

                //书籍分类
                catalog: {
                    popular: "热门图书",
                    newest: "最新首发",
                    novel: "小说",
                    literature: "文学",
                    art: "艺术",
                    biography: "传记",
                    philosophy: "哲学",
                    history: "历史",
                    politics: "政治",
                    culture: "文化",
                    computer: "计算机",
                    industry: "工业技术",
                    medicine: "医学",
                    science: "自然科学",
                    tourism: "旅游",
                    fashion: "时尚",
                    journey: "专业期刊",
                    education: "教育科普",
                    hinata: "同人",
                    action: "动作",
                    behold: "猎奇",
                    fantasy: "奇幻",
                    enlish: "少儿英语",
                    quiz: "成长益智",
                    tales: "儿童文学",
                    enlightened: "启蒙读物"
                },
                receivedBooks:[]
            }
            
        },
        computed: {
        showBooks () {
            console.log(this.receivedBooks);
            return this.receivedBooks[this.pageNumber - 1];
          }
        },
        mounted() {

            console.log("已经挂载");
            this.$Loading.start();
            this.bookLoading = true;
            this.$request.put('/api/book?type=popular')
                    .then((response) => {

                      
                      let state = response.data.state;
                      if (state) {
                        this.$Message.success("加载图书数据成功");

                        this.$Loading.finish();

                        this.receivedBooks = response.data.info;
                        this.resultsTotal = response.data.len;
                        this.noBook = false;
                        this.bookLoading = false;
                        this.hasBook = true;
                        this.$Notice.open({
                            title: '操作提示',
                            desc:'已打开图书简介显示，点击首页右上方按钮关闭'
                        });

                    }
                    else {
                        this.$Message.error("加载图书数据失败. Info: " + response.data.info, 3);
                        this.$Loading.error();
                        this.resultsTotal = 0;
                        this.bookLoading = false;
                        this.noBook = true;
                        this.hasBook = false;

                    }

                }).catch((error) => {
                  console.log(error);
                  this.$Loading.error();
                  this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                  this.$Message.error('服务器繁忙');
                  this.noBook = true;
                  this.bookLoading = false;
                  this.hasBook = false;
              }); 
            

        },
        methods: {
            checkUser() {
                if(this.$ls.get('userid', 0) == 0) {
                    this.$router.push('/login');
                }
            },
            mockData() {
                let data = [];
                for (let i = 0; i < 4; i++) {
                    data.push({
                        id:i + 2,
                        username: "test",
                        created_at: '2017-05-31 18:50:53',
                        content: "一本好书"
                    })
                };
                return data;ss


            },
            generateOrder () {
                this.checkUser();
                this.$Loading.start();
                this.generateOrderLoading = true;
                this.$request.post('/api/order',{
                    user_id:this.$ls.get('userid', 0),
                    pay_amount:this.orderBookNumber * arguments[0].price,
                    book_list:[arguments[0].id],
                    status:1
                })
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("生成订单成功, 请前往订单页面进行支付", 5);
                        this.$Loading.finish();
                        this.bookDetailsModal = false;

                        this.generateOrderLoading = false;

                    }
                    else {
                        this.$Message.warning("生成订单失败");
                        this.$Loading.finish();
                        this.generateOrderLoading = false;

                    }

                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.generateOrderLoading = false;

                    this.$Message.error('服务器繁忙');

                }); 

            },
            addIntoCart() {
                this.checkUser();
                this.addIntoCartLoading = true;
                // this.$Message.success(arguments[0]);
                this.$request.post('/api/cart?book_id='+arguments[0].id+"&user_id="+this.$ls.get('userid', 0)+"&qty="+this.orderBookNumber)
                    .then((response) => {

                      
                      this.addIntoCartLoading = false;
                      this.bookDetailsModal = false;
                      let state = response.data.state;
                      if (state) {
                        this.$Message.success("已将"+this.orderBookNumber+"本《" + arguments[0].name+ "》加入购物车成功");
                        this.$Loading.finish();
                    }
                    else {
                        this.$Message.error("加入购物车失败 " + "Info: " + response.data.info, 3);
                        this.$Loading.error();
                    }
                }).catch((error) => {
                  console.log(error);
                  this.$Loading.error();
                  this.addIntoCartLoading = false;
                  this.$Message.error("加入购物车失败. Info: 服务器繁忙", 3);
              });  
            }
            ,
            changePages() {
                
                this.pageNumber = arguments[0];
                
            },
            showBrief() {
                if (arguments[0]) {
                    this.$Message.success("已开启书籍简要介绍显示");
                }
                else {
                    this.$Message.success("已关闭书籍简要介绍显示");
                }
                this.showBriefIntro = arguments[0];
            },
            getBooks() {
                this.$Loading.start();
                this.bookLoading = true;
                this.receivedBooks =[[]];
                this.booksType = arguments[0];
                this.resultTitle = this.catalog[arguments[0]];
                if (arguments[0] == "popular" || arguments[0] == "newest") {
                   
                    this.$request.put('/api/book?type='+arguments[0])
                    .then((response) => {

                      let state = response.data.state;
                      if (state) {
                        this.$Message.success("加载图书数据成功");

                        this.$Loading.finish();

                        this.bookLoading = false;
                        this.receivedBooks = response.data.info;
                        this.resultsTotal = response.data.len;
                        this.noBook = false;
                        this.hasBook = true;

                    }
                    else {
                        this.$Message.error("加载图书数据失败 " + "Info: " + response.data.info, 3);
                        this.$Loading.error();
                        this.resultsTotal = 0;
                        this.bookLoading = false;
                        this.noBook = true;
                        this.hasBook = false;

                    }

                }).catch((error) => {
                  console.log(error);
                  this.$Loading.error();
                  this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                  this.noBook = true;
                  this.bookLoading = false;
                  this.hasBook = false;
              });  
                }

                else {

                 this.$request.patch('/api/book',{bookType:arguments[0]})
                 .then((response) => {

                  // console.log(response.data.info);
                  let state = response.data.state;
                  if (state) {
                    this.$Message.success("加载图书数据成功");

                    this.$Loading.finish();
                    
                    this.receivedBooks = response.data.info;
                    this.resultsTotal = response.data.len;
                    this.noBook = false;
                    this.bookLoading = false;
                    this.hasBook = true;
                    
                }
                else {
                    this.$Message.error("加载图书数据失败 " + "Info: " + response.data.info, 3);
                    this.$Loading.error();
                    this.resultsTotal = 0;
                    this.noBook = true;
                    this.bookLoading = false;
                    this.hasBook = false;
                    
                }

            }).catch((error) => {
              console.log(error);
              this.$Loading.error();
              this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
              this.noBook = true;
              this.bookLoading = false;
              this.hasBook = false;
          });
            



            }
               
            },
            buyBook() {
                this.$Message.success("购买了"+this.orderBookNumber+"本"+this.bookDetails.name);
                this.orderBookNumber = 1;
                this.bookDetailsModal = false;
            },
            searchBook() {
                this.bookLoading = true;
                this.resultTitle = "'" + this.search + "' 的搜索结果";
                this.$Loading.start();
                this.$request.patch('/api/book',{name:this.search})
                .then((response) => {

                  // console.log(response.data.info);
                  let state = response.data.state;
                  if (state) {
                    this.$Message.success("加载图书数据成功");

                    this.$Loading.finish();
                    this.receivedBooks = response.data.info;
                    this.noBook = false;
                    this.hasBook = true;
                    this.bookLoading = false;
                    this.resultsTotal = response.data.len;
                    
                  }
                  else {
                    
                    this.$Loading.error();
                    this.$Message.error("加载图书数据失败 " + "Info: " + response.data.info, 3);
                    this.noBook = true;
                    this.bookLoading = false;
                    this.resultsTotal = 0;
                    this.hasBook = false;
                  }

                }).catch((error) => {
                  console.log(error);
                  this.$Loading.error();
                  this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                  this.noBook = true;
                  this.bookLoading = false;
                  this.hasBook = false;
                });
               
            },
            showComments() {

            },
            enterBookDetails(book) {
                this.bookDetailsModal =true;
                this.bookDetails = book;
                this.isCommentLoading = true;
                this.$Loading.start()
                this.$request.get('/api/comment?book_id='+book.id)
                .then((response) => {
                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("获取订单信息成功");

                        this.$Loading.finish();
                        this.hasComment = true;
                        if (response.data.info.length == 0) {
                            this.hasComment = false;
                        }
                        
                        this.isCommentLoading = false;
                        
                       

                        this.comments = response.data.info.reverse();
                    }
                    else {
                        this.$Message.warning("当前没有订单");
                        this.$Loading.finish();

                        this.hasComment = false;
                        this.isCommentLoading = false;
                       

                    }

                }).catch((error) => {
                    console.log(error);
                    this.$Loading.error();
                    this.hasComment = false;
                    this.isCommentLoading = false;
                    this.$Message.error('服务器繁忙');

                }); 

            }
        },
        components: {
            "book": BookCard,
            "mugen-scroll": MugenScroll,
            Avatar
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .layout_home{
        position: relative;
        text-align: start;
        border-radius: 4px;
        /*overflow: hidden;*/
        white-space: nowrap;
        /*border: 1px solid #d7dde4;*/
        min-height: 700px;
    }

    p {
        font-size: 30px;
        margin: 25px;
        color: #FF4136;
        margin-bottom:20px;

    }

    .content {
        padding:20px;
        /*position: relative;*/
        width: 100%;
        min-height: 500px;
        /*background-color: #aaaaaa;*/
    }

    .bookCover {
        width: 80%;
        margin: 40px;
        border-radius: 2px;
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    }

    .bookDetails {
       
        border-radius: 2px;
        width: 100%;
       

    }

    .shadow {

         box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    }

    .active {
        height: 500px;
    }

    .bookscontent {

    }
    .home_display {
        margin: 25px;
        margin-left:75px;
        margin-right: 75px; 
    }

    .demo-carousel {
        height: 300px;
        background: #bbbbbb;
    }

    .bookList {
        border: 1px solid #d7dde4;
        min-height: 630px;

    }
    .vertical{
        display: flex;
       
        align-items:center;
        display:-webkit-flex;
    }

    .commentItem {

        margin-bottom: 10px;
        border-radius: 5px;
        transition:all .3s ease-in-out;
        border: 1px solid #d7dde4;
        

    }

    .commentItem:hover {
       /* margin-top: -1px;*/
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
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

    .tableColumn {
        font-size: 8px;
        color: #999
    }
    .commentItemHeader {
        height: 20px;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .commentItemContent {

    }

    .comment {
        font-size: 16px;
        color: #999;
    }

    .commentUsername {
        font-size: 16px;
        color: #bbb;
    }
    .commentItemWrapper {
       /* transition: all 0.5s;
        
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);*/
    }



    .commentItemWrapper:hover {
        /*margin-top: -1px;*/
        /*border: 1px solid #d7dde4;*/
    }



</style>