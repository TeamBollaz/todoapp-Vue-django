<template>
  <div >
    <div >
      <div></div>
      <h4>Edit User</h4>
      <span class="msgs"></span>

      <form @submit.prevent="updateUser" >
        <div  class="form-group row">
          <input
            type="text"
            name="username"
            v-model="form.username"
            placeholder="Username"
            class="form-control"
            autofocus
            required
            id="id_username"
          >
        </div>
        <span></span>
        <div  class="form-group row">
          <input
            type="email"
            name="email"
            v-model="form.email"
            placeholder="Email"
            class="form-control"
            required
            id="id_email"
          >
        </div>
        <span></span>
        <button type="submit" class="button" name="update">Update</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'UserRegister',
  data () {
    return {
      form: {
        username: '',
        email: ''
      }
    }
  },
  mounted () {
    this.getUsers()
  },
  methods: {
    getUsers () {
      axios
        .get(`/api/users/${this.$route.params.id}`)
        .then(res => {
          this.form = res.data
          console.log(res)
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateUser () {
      axios
        .put('/api/users/' + this.$route.params.id + '/', {
          username: this.form.username,
          email: this.form.email
        })
        .then(res => {
          this.$router.push({ name: 'Users' })
        })
    }
  }
}
</script>

<style >
</style>
