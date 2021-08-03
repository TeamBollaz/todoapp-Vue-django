<template>
  <div id="Fruits">
    <div class="sec-header">
      <div class="sec-title">Fruits</div>
      <div class="crumbs">Dashboard > fruits</div>
    </div>
    <div class="main-c">
      <div class="mheader">
        <div class="back">
          <router-link :to="{name: 'FruitsCreate'}">
            <button class="button" >Add Fruit</button>
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="showMessage">
      <div class="alert alert-success" role="alert">{{ message }}</div>
    </div>
    <div class="mmain">
      <table
        class="table table-bordered table-striped tables dt-responsive dataTable no-footer dtr-inline"
      >
        <thead>
          <tr>
            <th>Id</th>
            <th>Fruit Name</th>
            <th>Fruit Type</th>
            <th>WHERE FOUND(Region)</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody v-for="fruit in fruits" v-bind:key="fruit.id">
          <td>{{ fruit.id }}</td>
          <td>{{ fruit.fruitname }}</td>
          <td>{{ fruit.ftype }}</td>
          <td>{{ fruit.region }}</td>
          <td>
            <router-link :to="{name: 'FruitEdit', params:{id: fruit.id}}"><button @click="getFruit(fruit.id)"><i class="fa fa-pencil" ></i></button></router-link>
            <button @click="deleteFruit(fruit.id)">
              <i class="fa fa-trash-o"></i>
            </button>
          </td>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Fruits',
  data () {
    return {
      fruits: []
    }
  },
  mounted () {
    this.getFruits()
  },
  methods: {
    getFruits () {
      axios
        .get('/apifruit/fruits/')
        .then(res => {
          this.fruits = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getFruit (id) {
      axios
        .get('/apifruit/fruits/' + id)
        .then(res => {
          this.fruits = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteFruit (id) {
      axios
        .delete('/apifruit/fruits/' + id)
        .then(res => {
          this.showMessage = true
          this.message = res.data
          this.getFruits()
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style >
</style>
