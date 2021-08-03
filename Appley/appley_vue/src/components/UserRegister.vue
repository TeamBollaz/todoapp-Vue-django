<template>
  <div >
    <div >
      <div></div>
      <h4>Register User</h4>
      <span class="msgs"></span>

      <form @submit.prevent="storeUser">
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
        <div  class="form-group row">
          <input
            type="password"
            name="password1"
            v-model="form.password"
            placeholder="Password"
            class="form-control"
            required
            id="id_password1"
          >
        </div>
        <button class="button" type="submit" name="register">Register</button>
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
        email: '',
        password: ''
      }
    }
  },
  methods: {
    storeUser () {
      axios
        .post('/api/users/', {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password
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
