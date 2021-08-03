<template>
  <div id="Users" >
    <div class="sec-header">
      <div class="sec-title">Users</div>
      <div class="crumbs">Dashboard > users</div>
    </div>
    <div class="main-c">
      <div class="mheader">
        <div class="back">
          <router-link :to="{name: 'UserRegister'}"><button class="button" > Add User</button></router-link>
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
            <th>UserName</th>
            <th>User Email</th>
            <th>Action</th>
          </tr>
        </thead>

          <tbody v-for="user in users" v-bind:key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>
              <router-link v-bind:to="{name: 'UserEdit', params:{id: user.id}}"><button @click="getUser(user.id)" ><i class="fa fa-pencil" ></i></button></router-link>
              <button @click="deleteUser(user.id)" ><i class="fa fa-trash-o" ></i></button>
            </td>
          </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'User',
  data () {
    return {
      users: []
    }
  },
  mounted () {
    this.getUsers()
  },
  methods: {
    getUsers () {
      axios
        .get('/api/users/')
        .then(res => {
          this.users = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getUser (id) {
      axios
        .get('/api/users/' + id + '/')
        .then(res => {
          this.users = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteUser (id) {
      axios
        .delete('/api/users/' + id + '/')
        .then(res => {
          this.showMessage = true
          this.message = res.data
          this.getUsers()
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
