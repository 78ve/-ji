<template>
	<Form ref="form" :model="form" :label-width="100" :rules="topUpRule"  style="height:100px;margin:20px; padding-right:100px;">


  

		<Form-item label="输入金额" prop="amount">



            <Input-number   @on-change="getAmount" v-model="form.amount" placeholder="请输入金额" ></Input-number> 元
        </Form-item>
        <div>
        <p style="margin-top:50px;">Ps. 限于无法介入支付系统，在本次实验对充值，以及提现等功能做了简化</p>
  </div>
	</Form>
</template>

<script>
  export default {
    name: 'topup',
    data () {
      return {
        self: this,
        form: {
          amount:0,
        },
        topUpRule: {
          amount: [
          { required:true, trigger: 'blur'}
          ],
        }
      }
    },
    methods: {
      getAmount() {
        this.$emit('transferAmount', this.form);
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