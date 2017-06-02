<template>
    <div class="book-row">


        <Row  type="flex" justify="start"  >
            <!-- <transition-group   
            name="bounce"
            mode="out-in"
            enter-active-class="bounceInLeft"
            leave-active-class="bounceOutRight" tag="ul"> -->
            <Col style=" margin-top:20px;" span="6" v-for="(book, index) in booksInfo" :key="book.id" >

                <div style="text-align:center" @click="showDetails(book)">
                    <Card :padding="8" class="bookCard" >
                    <div >
                        <Poptip v-if="showBriefIntro"  trigger="hover" placement="right">
                            <div  slot="content" style="white-space:normal">
                                <p>{{book.briefInfo}}</p>
                            </div>
                            <img class="bookCover" :src="book.cover">
                        </Poptip>

                        <img v-if="! showBriefIntro" class="bookCover" :src="book.cover">
                         <div  class="bookTitle ">
                                        {{book.name}}
                                    </div>
                        <div class="bookFooter"> 
                            <Row type="flex"  align="bottom" >
                                <Col span="12">
                                    <div  class="bookAuthor ">
                                    {{book.author}}
                                </div>

                                </Col>
                                
                                <Col :offset="2" span="10">
                                     <div  class="bookPrice ">
                                         ￥<span class="price">{{book.price}}</span>
                                     </div>

                                </Col>
                            </Row>

                            

                            
                            
                            
                            
                        </div>

                    </div>
                </Card>
                    

                </div>
                


            </Col>
       <!--  </transition-group> -->
    </Row>



</div>

</template>

<script>
  export default {
    props: ['booksInfo','showBriefIntro'],
    data () {
      return {
        spanLeft: 4
    }

},

methods: {
    showDetails(book) {
        this.$Message.success(book.id);
        this.$emit('transferSelectBookInfo', book);
    }
}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bookCover {
    width: 100%;
    height: 212px;

    border-radius: 4px;
    background-color: #bbbbbb;
    transition:all .3s ease-in-out;
    box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, .10), 0px 0px 1px 0px rgba(0, 0, 0, .04)

}

.bookCover:hover {

    -webkit-filter:brightness(.95) ;
}
.bookCard:hover {
    /*margin-top: -1px;*/
     /*-webkit-filter:brightness(.95) ;*/
    box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, .10), 0px 0px 12px 0px rgba(0, 0, 0, .04);
    transition:all .3s ease-in-out;
    
}

.bookCard {
    width:180px;
    transition:all .3s ease-in-out;
    border-radius: 4px;
    margin-bottom: 20px;
    margin-right: auto; 
    margin-left: auto; 

    
}
.bookTitle {
    text-align: start;
    margin-top:5px; 
    margin-bottom: 5px;
    font-size: 14px;
    transition:all .3s ease-in-out;
    
    margin-left: 10px;
    overflow:hidden; 
    text-overflow:ellipsis;
    white-space:nowrap; 
    width:10em; 

}

.bookTitle:hover {
    color: #FF4136;

}
.bookAuthor {
    font-size: 12px;
    color: #aaaaaa;
    white-space:nowrap; 
    width:5em; 
    margin-left: 10px;
    overflow:hidden; 
    text-overflow:ellipsis;
    text-align:start;


}

.bookFooter {

}

.bookPrice {

    text-align: end;

}

.price {
    font-size: 16px;
    font-weight: bolder;
    color:#FF4136;
}

.ivu-poptip-body-content-inner {
    white-space: normal;
}

.book-row {
   /* background-color: #353535;*/
   
}

</style>