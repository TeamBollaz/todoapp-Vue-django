<template>
  <div>
    <div>
      <div></div>
      <h4>Add Fruit</h4>
      <span class="msgs"></span>

      <form @submit.prevent="storeFruit">
        <div  class="form-group row">
          <input
            type="text"
            name="fruitname"
            v-model="form.fruitname"
            placeholder="fruitname"
            class="form-control"
            autofocus
            required
            id="id_fruitname"
          >
        </div>
        <span></span>
        <div  class="form-group row">
          <input
            type="text"
            name="ftype"
            v-model="form.ftype"
            placeholder="ftype"
            class="form-control"
            required
            id="id_ftype"
          >
        </div>
        <span></span>
        <span></span>
        <div  class="form-group row">
          <input
            type="text"
            name="region"
            v-model="form.region"
            placeholder="region"
            class="form-control"
            required
            id="id_region"
          >
        </div>
        <span></span>
        <button class="button" type="submit" name="Add">Add</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FruitsCreate',
  data () {
    return {
      form: {
        fruitname: '',
        ftype: '',
        region: ''
      }
    }
  },
  methods: {
    storeFruit () {
      axios
        .post('/apifruit/fruits/', {
          fruitname: this.form.fruitname,
          ftype: this.form.ftype,
          region: this.form.region
        })
        .then(res => {
          this.$router.push({ name: 'Fruits' })
        })
    }
  }
}
</script>

<style >
</style>
