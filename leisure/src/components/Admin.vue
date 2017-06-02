<template>
    <div class="layout_home" >


        <div>
            <Row type="flex"  justify="start"  >
                <Col  span="4">
                    <p class="tabTitle">管理面板</p>

                </Col>

            </Row>
        </div>

        <div>
            <hr width=100% size=3 color=#eeeeee style="FILTER: alpha(opacity=100,finishopacity=0,style=3); margin-bottom:20px;"> 
        </div>





        <div>
            <Tabs  value="name1">
                <Tab-pane label="用户管理" name="name1">



                   <Row  type="flex"  justify="end"  style="margin-bottom:20px;">

                        <Col  class="vertical" span="6" >

                            <div >
                                <Page :total="userTotal" :current="usersPageNumber" @on-change="changeUsersPages" size="small" show-total></Page>
                            </div>

                        </Col>
                    </Row>
                    <div class="userManagement">




                        <Row  type="flex"  justify="center" class="userTitle">
                            <Col   span="20">

                                <Row  type="flex" justify="center"  style="margin-bottom:20px;" >
                                    <Col  class="vertical"  span="2"  >
                                        <Checkbox
                                        :indeterminate="indeterminate"
                                        :value="checkAll"
                                        @click.prevent.native="handleCheckAll"
                                        ></Checkbox>
                                        <p  class="tableColumn">全选</p>
                                    </Col>
                                    <Col class="vertical" span="2"  >
                                    <p class="tableColumn" >用户ID</p>
                                    </Col>
                                    <Col  class="vertical" span="1"  >
                                    <p class="tableColumn" >头像</p>
                                    </Col>

                                    <Col  :offset="1"  class="vertical" span="2"  >
                                        <p  class="tableColumn">用户名</p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="2" >
                                        <p  class="tableColumn">用户创建日期</p>
                                    </Col> 
                                    <Col  offset="1" class="vertical"  span="2" >
                                        <p  class="tableColumn">用户类型</p>
                                    </Col> 
                                    <Col :offset="1" class="vertical"  span="3" >
                                        <p  class="tableColumn">余额</p>
                                    </Col>
                                    <Col :offset="1" class="vertical"  span="5" >
                                        <Button-group style=""  shape="circle">
                                                    <Button type="primary"  @click="createAccountForm = true">
                                                     添加
                                                 </Button>
                                        </Button-group>
   
                                    </Col>
                                </Row>

                            </Col>
                        </Row>


                        <Row  type="flex"  justify="center">
                            <Col  span="20">
                                <transition-group name="list-complete">
                                    <div class="list-complete-item" v-if="hasUser" style="width:100%;"  v-for="user in showUsers" :key="user">


                                        <div >
                                            
                                            <Row  type="flex" justify="center" class="userItem" >
                                                <Col  class="vertical"  span="2"  >
                                                    <Checkbox></Checkbox>
                                                    
                                                </Col>
                                                <Col class="vertical" span="2"  >
                                                    <p class="tableColumn" >{{user.id}}</p>
                                                </Col>
                                                <Col  class="vertical" span="1"  >
                                                    <avatar :username="user.name"
                                                    class="avatar"
                                                    background-color="#FFC107"
                                                    :size="40"></avatar>
                                                </Col>

                                                <Col  :offset="1"  class="vertical" span="2" >
                                                <p  class="tableColumn">{{user.name}}</p>
                                                </Col>
                                                <Col :offset="1" class="vertical"  span="2"  >
                                                    <p  class="tableColumn">{{user.created_at}}</p>
                                                </Col> 
                                                 <Col offset="1" class="vertical"  span="2"  >
                                                    <tag v-if="user.userLevel" class="tableColumn">管理员</tag>
                                                    <tag v-if="! user.userLevel" class="tableColumn">普通用户</tag>
                                                </Col> 
                                                <Col :offset="1" class="vertical"  span="3"  >
                                                    <p  class="tableColumn">￥<span style="color:#FF4136">{{user.balance}}</span></p>
                                                </Col>
                                                <Col :offset="1" class="vertical"  span="5"  >
                                                     <Button-group style=""  shape="circle">
                                                    <Button type="ghost" @click="removeUser(user.id)">
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


                    </div>



                </Tab-pane>
                <Tab-pane label="书籍管理" name="name2">

                   <Row  type="flex"  justify="end"  style="margin-bottom:20px;margin-top:30px;">
                     <Col  class="vertical"  span="4" >

                        <div >
                             <Cascader :data="bookTypeData" :load-data="loadBookTypeData"></Cascader>
                        </div>

                    </Col>
                        <Col  class="vertical" span="6" >

                            <div >
                                <Page :total="bookTotal" :current="booksPageNumber" @on-change="changeBooksPages" size="small" show-total></Page>
                            </div>

                        </Col>
                    </Row>

                    <div class="bookManagement">
                        <Row  type="flex"  justify="center" class="bookTitle">
                            <Col   span="20">

                                <Row  type="flex" justify="center"  >
                                    <Col  class="vertical"  span="2"  >
                                        <Checkbox
                                        :indeterminate="indeterminate"
                                        :value="checkAll"
                                        @click.prevent.native="handleCheckAll"
                                        ></Checkbox>
                                        <p  class="tableColumn">全选</p>
                                    </Col>
                                    <Col class="vertical" span="1"  >
                                    <p class="tableColumn" >ID</p>
                                    </Col>
                                    <Col  class="vertical" span="3"  >
                                    <p class="tableColumn" >书名</p>
                                    </Col>

                                    <Col    class="vertical" span="2"  >
                                        <p  class="tableColumn">作者</p>
                                    </Col>
                                    <Col    class="vertical" span="3"  >
                                        <p  class="tableColumn">简介</p>
                                    </Col>
                                    <Col  class="vertical"  span="2" >
                                        <p  class="tableColumn">价格(元)</p>
                                    </Col> 
                                    <Col  class="vertical"  span="2" >
                                        <p  class="tableColumn">销量(本)</p>
                                    </Col> 
                                     <Col  class="vertical"  span="2" >
                                        <p  class="tableColumn">封面</p>
                                    </Col>
                                    <Col class="vertical"  span="2" >
                                        <p  class="tableColumn">详情</p>
                                    </Col>
                                    <Col  class="vertical"  span="4" >
                                        <p  class="tableColumn">操作</p>
   
                                    </Col>
                                </Row>

                            </Col>
                        </Row>


                        <Row  type="flex"  justify="center">
                            <Col  span="20">
                                <transition-group name="list-complete">
                                    <div class="list-complete-item" v-if="hasBook" style="width:100%;"  v-for="book in showBooks" :key="book">


                                        <div >
                                            
                                            <Row  type="flex" justify="center" class="userItem" >
                                                <Col  class="vertical"  span="2"  >
                                                    <Checkbox></Checkbox>
                                                    
                                                </Col>
                                                <Col class="vertical" span="1"  >
                                                    <p class="tableColumn" >{{book.id}}</p>
                                                </Col>
                                                <Col  class="vertical" span="3"  >
                                                    <p class="tableColumn" >{{book.name}}</p>
                                                </Col>

                                                <Col    class="vertical" span="2"  >
                                                    <p  class="tableColumn">{{book.author}}</p>
                                                </Col>
                                                <Col    class="vertical" span="3"  >
                                                <Poptip trigger="hover" title="提示标题" content="提示内容">

                                                    <div  slot="content" style="white-space:normal">
                                                            <p  class="tableColumn">{{book.briefInfo}}</p>
                                                    </div>
                                                     <tag  class="tableColumn">查看简介</tag>
                                                    </Poptip>
                                                    
                                                </Col>
                                                <Col  class="vertical"  span="2" >
                                                    <p  class="tableColumn">￥<span style="color:#FF4136">{{book.price}}</span></p>
                                                </Col> 
                                                <Col  class="vertical"  span="2" >
                                                    <p  class="tableColumn">{{book.salesVolume}}</p>
                                                </Col> 
                                                <Col  class="vertical"  span="2" >
                                                    <Poptip trigger="hover" title="提示标题" content="提示内容">

                                                    <div  slot="content">
                                                            <img class="bookCover" :src="book.cover">
                                                    </div>
                                                     <tag  class="tableColumn">查看封面</tag>
                                                    </Poptip>
                                                  
                                                </Col>
                                                <Col class="vertical"  span="2" >
                                                    <Tooltip content="点击显示详情长图">
                                                        <a :href="book.details" class="tableColumn" target="_blank">详情</a>
                                                    </Tooltip>
                                                
                                                </Col>
                                                <Col  class="vertical"  span="4" >
                                                     <Button-group style=""  shape="circle">
                                                    <Button type="ghost">
                                                     编辑
                                                 </Button>
                                                 <Button type="ghost" >
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


                    </div>
            

                </Tab-pane>
            </Tabs>

        </div>


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




    </div>
</template>

<script>
    import LoginForm from "../forms/LoginForm"
    import Avatar from 'vue-avatar/dist/Avatar'
    export default {
        data () {
            return {
                logoTitle: "Melody",
                show: true,



                checkAll:false,
                indeterminate:false,

                //用户管理
                users:[],
                hasUser:true,
                noUser: false,
                userTotal:0,
                usersPageNumber:1,
                newAccountInfo:{},
                createAccountForm:false,

                //书籍管理
                bookTotal:0,
                books:[],
                booksPageNumber:1,
                hasBook:true,
                noBook: false,



                bookTypeData:[
                    {
                        value: 'wenyi',
                        label: '文艺',
                        children: [],
                        loading: false
                    },
                    {
                        value: 'renwensheke',
                        label: '人文社科',
                        children: [],
                        loading:false
                    },
                    {
                        value: 'keji',
                        label: '科技',
                        children: [],
                        loading:false
                    },
                    {
                        value: 'qikanzazhi',
                        label: '期刊杂志',
                        children: [],
                        loading:false
                    },
                    {
                        value: 'manhua',
                        label: '漫画',
                        children: [],
                        loading:false
                    },
                    {
                        value: 'ertongduwu',
                        label: '儿童读物',
                        children: [],
                        loading:false
                    }
                ],


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
                return this.books[this.booksPageNumber - 1];
            },

            showUsers () {
                console.log(this.receivedBooks);
                return this.users[this.usersPageNumber - 1];
            }
        },
        mounted() {

            console.log("已经挂载");

            this.$Loading.start();

            this.$request.get('/api/user')
            .then((response) => {


                let state = response.data.state;
                if (state) {
                    this.$Message.success("加载用户数据成功");

                    this.$Loading.finish();

                    this.users = response.data.info;
                    this.userTotal = response.data.len;
 
                    this.$Loading.start();

                    this.$request.post('/api/book')
                    .then((response) => {


                        let state = response.data.state;
                        if (state) {
                            this.$Message.success("加载图书数据成功");

                            this.$Loading.finish();

                            this.books = response.data.info;
                            this.bookTotal = response.data.len;

                        }
                        else {
                            this.$Message.error("加载图书数据失败. Info: " + response.data.info, 3);
                            this.$Loading.error();
                        }

                    }).catch((error) => {
                        console.log(error);
                        this.$Loading.error();
                        this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                        this.$Message.error('服务器繁忙');

                    }); 
                }
                else {
                    this.$Message.error("加载用户数据失败. Info: " + response.data.info, 3);
                    this.$Loading.error();
                }
            }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                this.$Message.error('服务器繁忙');
            }); 
        },
        methods: {
          setNewAccountInfo(msg) {
            this.newAccountInfo = msg;
        },
            checkUser() {
                if(this.$ls.get('userid', 0) == 0) {
                    this.$router.push('/login');
                }
            },
            removeUser() {
                this.checkUser();
                this.$request.delete('/api/user?user_id='+arguments[0])
                .then((response) => {


                    let state = response.data.state;
                    if (state) {
                        this.$Message.success("删除用户成功");
                        

                        this.$request.get('/api/user')
                        .then((response) => {


                            let state = response.data.state;
                            if (state) {
                                this.$Message.success("加载用户数据成功");

                                this.$Loading.finish();

                                this.users = response.data.info;
                                this.userTotal = response.data.len;


                            }
                            else {
                                this.$Message.error("加载用户数据失败. Info: " + response.data.info, 3);
                                this.$Loading.error();
                            }
                        }).catch((error) => {
                            console.log(error);
                            this.$Loading.error();
                            this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                            this.$Message.error('服务器繁忙');
                        });            
                    }
                    else {
                        this.$Message.error("删除用户失败")
                        this.$Message.error(response.data.info,5);
                        this.$Loading.error();
                    }

                }).catch((error) => {
                    console.log(error);
                    this.$Message.error(error);
                });
            },
            createAccount() {
                this.checkUser();       
                this.$Loading.start();
                if (!this.newAccountInfo.username) {
                  this.$Loading.error();
                  this.$Message.error('注册失败');
                  return false;
              }
              this.$request.post('/api/user', {
                  "username": this.newAccountInfo.username,
                  "password": this.newAccountInfo.password
              })
              .then((response) => {


                let state = response.data.state;
                if (state) {
                    this.$Message.success("添加用户成功");
             this.$request.get('/api/user')
            .then((response) => {


                let state = response.data.state;
                if (state) {
                    this.$Message.success("加载用户数据成功");

                    this.$Loading.finish();

                    this.users = response.data.info;
                    this.userTotal = response.data.len;

                    
                }
                else {
                    this.$Message.error("加载用户数据失败. Info: " + response.data.info, 3);
                    this.$Loading.error();
                }
            }).catch((error) => {
                console.log(error);
                this.$Loading.error();
                this.$Message.error("加载图书数据失败. Info: 服务器繁忙", 3);
                this.$Message.error('服务器繁忙');
            });                    

                }
                else {
                    this.$Message.error("添加用户失败" + response.data.info,5);
                    this.$Loading.error();
                }

            }).catch((error) => {
              console.log(error);
              this.$Message.error(error);
          });


            this.$refs.login_form.$refs.form.resetFields();

        },


            cancel() {
                this.$refs.login_form.$refs.form.resetFields();
                this.$Message.info("取消添加用户")
            },
            loadBookTypeData(item, callback) {
                item.loading = true;
                setTimeout(() => {
                    if (item.value === 'wenyi') {
                        item.children = [
                            {
                                value: 'novel',
                                label: '小说'
                            },
                            {
                                value: 'literature',
                                label: '文学'
                            },
                            {
                                value: 'art',
                                label: '艺术'
                            },
                            {
                                value: 'biography',
                                label: '传记'
                            }
                        ];
                    } else if (item.value === 'renwensheke') {
                        item.children = [
                            {
                                value: 'novel',
                                label: '哲学'
                            },
                            {
                                value: 'history',
                                label: '历史'
                            },
                            {
                                value: 'politics',
                                label: '政治'
                            },
                            {
                                value: 'culture',
                                label: '文化'
                            }
                        ];
                    } else if (item.value === 'keji') {
                        item.children = [
                            {
                                value: 'computer',
                                label: '计算机'
                            },
                            {
                                value: 'industry',
                                label: '工业技术'
                            },
                            {
                                value: 'medicine',
                                label: '医学'
                            },
                            {
                                value: 'science',
                                label: '自然科学'
                            }
                        ];
                    } else if (item.value === 'qikanzazhi') {
                        item.children = [
                            {
                                value: 'tourism',
                                label: '旅游'
                            },
                            {
                                value: 'fashion',
                                label: '时尚'
                            },
                            {
                                value: 'journey',
                                label: '专业期刊'
                            },
                            {
                                value: 'education',
                                label: '教育科普'
                            }
                        ];
                    } else if (item.value === 'manhua') {
                        item.children = [
                            {
                                value: 'hinata',
                                label: '同人'
                            },
                            {
                                value: 'action',
                                label: '动作'
                            },
                            {
                                value: 'behold',
                                label: '猎奇'
                            },
                            {
                                value: 'fantasy',
                                label: '奇幻'
                            }
                        ];
                    } else if (item.value === 'ertongduwu') {
                        item.children = [
                            {
                                value: 'enlish',
                                label: '少儿英语'
                            },
                            {
                                value: 'quiz',
                                label: '成长益智'
                            },
                            {
                                value: 'tales',
                                label: '儿童文学'
                            },
                            {
                                value: 'enlightened',
                                label: '启蒙读物'
                            }
                        ];
                    }
                    item.loading = false;
                    callback();
                }, 1000);
            },
            mockData1 () {
                let data = [];
                for (let i = 0; i < 10; i++) {
                    data.push({
                        id:i + 2,
                        name: "test",
                        price:"121.1",
                        author:"Alecysu",
                        salesVolume:100,
                        briefInfo:"asdddddddddddsasdsd",
                        cover: 'http://oqnxnowx3.bkt.clouddn.com/test.jpg',
                        details: "http://oqnxnowx3.bkt.clouddn.com/99999990001301807_1_o.jpg",
                        bookType:"literature"
                    })
                };
                return data;
            },
            changeBooksPages() {
                this.$Message.success(this.booksPageNumber);
                this.booksPageNumber= arguments[0];

            },
            changeUsersPages() {
                this.$Message.success(this.usersPageNumber);
                this.usersPageNumber= arguments[0];

            },
            getData() {
 
            },
            mockData() {
                let data = [];
                for (let i = 0; i < 10; i++) {
                    data.push({
                        id:i + 2,
                        username: "test",
                        created_at: '2017-05-31 18:50:53',
                        balance: "121142"
                    })
                };
                return data;
            },
            changePages() {
                this.$Message.success(this.pageNumber);
                this.pageNumber = arguments[0];

            },
            getData() {
 
            }
        },
        components: {
            "LoginForm": LoginForm,
            Avatar
        }

    }
</script>


<style scoped>
    .layout_home{

        border-radius: 4px;
        margin: 50px;
        margin-top:20px;

        min-height: 700px;
    }
    .tabTitle {
        font-size: 30px;
        margin: 25px;
        color: #FF4136;
        margin-bottom:20px;

    }

    .userItem {
        margin-bottom: 10px;
        transition:all .3s ease-in-out;
        border: 1px solid #d7dde4;
        
        margin-bottom: 10px;
        border-radius: 4px;
        min-height: 60px
        
    }


    .userItem:hover {
        /* margin-top: -1px;*/
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
        transition:all .3s ease-in-out;

    }

    .userManagement {
       
        min-height: 500px;
    }

    .bookManagement {
       
        min-height: 400px;

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

    .userTitle {
        margin-bottom: 5px;
    }
    .bookTitle {
        margin-bottom: 20px;
    }

    .bookCover {
        width: 95%;
        height: 95%;
        box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, .10), 0px 0px 4px 0px rgba(0, 0, 0, .04);
    }
</style>