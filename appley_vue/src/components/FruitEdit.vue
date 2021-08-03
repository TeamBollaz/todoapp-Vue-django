<template>
  <div class="row justify-content-center" >
    <div class="card-body">
      <div></div>
      <h4>Edit Fruit Details </h4>
      <span class="msgs"></span>

      <form @submit.prevent="updateFruit">
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
        <button type="submit" name="Add">Edit</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FruitEdit',
  data () {
    return {
      form: {
        fruitname: '',
        ftype: ''
      }
    }
  },
  mounted () {
    this.getFruits()
  },
  methods: {
    getFruits () {
      axios
        .get(`/apifruit/fruits/${this.$route.params.id}`)
        .then(res => {
          this.form = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateFruit () {
      axios
        .put('/apifruit/fruits/' + this.$route.params.id + '/', {
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
