<template>
    <div class="layout">

        <Affix>
        <Menu class="menu" mode="horizontal" @on-select="changeRouter" theme="light">
            <div class="layout-logo" >
                
               <!--   -->

                <Row>
                    
                    <Col span='2'>
                        <icon style="margin-top:6px;margin-left:20px;" name="logo1" scale="5"></icon>
                    </Col>

                    <Col span='1'>
                         <p>{{logoTitle}}</p>
                         
                    </Col>
                </Row>

            </div>
            <div class="layout-nav">
                <Row type="flex" justify="end" >
                    
                    <Col span="2">
                        <Menu-item  name="">
                            <Icon type="ios-home"></Icon>
                            首页
                        </Menu-item>
                    </Col>
                    <Col span="2">
                        
                        <Menu-item name="cart" >
                        
                            <Icon type="ios-cart"></Icon>
                            
                            购物车
                        </Menu-item>
                    </Col>
                    <Col span="2">
                        <Menu-item name="order">
                            <Icon type="ios-paper"></Icon>
                            订单
                        </Menu-item>

                    </Col>
                    <Col v-if="userLevel" span="2">
                        <Menu-item name="admin">
                            <Icon type="ios-paper"></Icon>
                            管理
                        </Menu-item>
                    </Col>

                    <Col span="2">

                        <Dropdown style="margin-left: 10px"    @on-click="changeRouter" >
                            <avatar :username="username"
                            class="avatar"
                            background-color="#FFC107"
                            :size="40"></avatar>
                            <Dropdown-menu slot="list" >
                                <Dropdown-item name="userinfo">个人信息</Dropdown-item>
                                <Dropdown-item name="">预留项</Dropdown-item>
                                <Dropdown-item divided name="quit">退出登录</Dropdown-item>
                            </Dropdown-menu>
                        </Dropdown>

                    </Col>
                    <Col span="">
                        <span>{{username}}</span>
                    </Col>
                </Row>
            </div>
        </Menu>

        </Affix>

        <!-- 轮播组件 -->



        <div class="layout-content">


            <transition name="component-fade" mode="out-in" appear>
                <router-view></router-view>
            </transition>

        </div>

        <Back-top></Back-top>
        <div class="layout-copy">
            Copyright &copy; 2017 Leisure BookStore
        </div>
        <Back-top></Back-top>


    </div>
</template>

<script>
    import Avatar from 'vue-avatar/dist/Avatar'
    export default {
        data () {
            return {

                logoTitle: "Leisure",
                show: true,
                value2: 0,
                
                username: "",
                userId:0,
                userLevel:0

            }

        },
        components: {
            Avatar
        },
        mounted() {
            this.username = this.$ls.get('username', "null");
            this.userLevel = this.$ls.get('userlevel', "null");
        },
        methods: {
            changeRouter () {
                if (arguments[0] == "quit") {
                    this.$ls.set('userid', 0);
                    this.$ls.set('username', '');

                    this.$router.push('/login');
                }
                else{
                    this.$router.push('/'+arguments[0]);
                }
            }
        }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    .menu {
        box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .05), 0px 0px 8px 0px rgba(0, 0, 0, .04);
    }
    .layout{
        border: 1px solid #d7dde4;
        background: #ffffff;
    }
    .layout-logo{
        width: 200px;
        height: 60px;
        /* background: #5b6270;*/
        border-radius: 3px;
        float: left;
        position: relative;

    }

    p {
        font-family: "Vladimir Script";
        font-weight: normal;
        font-size: 40px;
        color: #E45340;
        margin: 0 auto;
        margin-left: 60px;

    }
    span {
        margin-right:100px; 
        font-size: 20px
    }
    .layout-nav{
        /* width: 420px;*/
        margin: 0 auto;
    }
    .layout-assistant{
        width: 300px;
        margin: 0 auto;
        height: inherit;
    }
    .layout-breadcrumb{
        padding: 10px 15px 0;
    }
    .layout-content{
        min-height: 600px;
        margin: 50px;
        margin-top:10px;
        background: #ffffff;

    }
    .layout-content-main{
        padding: 10px;
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
    }



    .demo-carousel {
        height: 300px;
        background: #bbbbbb;
    }

    .home_display {
        margin: 25px;
        margin-left:75px;
        margin-right: 75px; 
    }

    .avatar {
        margin: 10px auto;
        margin-left:25px;
    }


.ivu-select-dropdown {
        position: relative!important;
}
</style>