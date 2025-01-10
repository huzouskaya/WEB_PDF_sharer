<template>
    <div>
      <h1>Регистрация</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Имя пользователя:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
      <div v-if="message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        message: ''
      };
    },
    methods: {
      async register() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            username: this.username,
            password: this.password
          });
          this.message = response.data.message;
        } catch (error) {
          this.message = 'Ошибка регистрации: ' + error.response.data;
        }
      }
    }
  };
  </script>