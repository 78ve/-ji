<template>
  <Form ref="form" :model="form" :label-width="100" :rules="commentRule"  style="height:150px;margin:20px; padding-right:100px;">
    <Form-item label="输入评论内容" prop="comment">      
      <Input @on-change="getComment" v-model="form.comment" type="textarea" :rows="4" placeholder="请输入..."></Input>
    </Form-item>
    <Form-item label="评分" prop="rate">

       <Rate @on-change="getComment" v-model="form.rate"></Rate>
    </Form-item>

    
  </Form>
</template>

<script>
  export default {
    name: 'comment',
    data () {
      return {
        self: this,
        form: {
          comment:"",
          rate:0
        },
        commentRule: {
          comment: [
          { required:true, trigger: 'blur'}
          ],
          rate: [
          { required:true, trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      getComment() {
        this.$emit('transferComment', this.form);
      }
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .ivu-select-dropdown {
    position: absolute !important;
  }
</style>