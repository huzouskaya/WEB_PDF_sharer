<template>
    <div>
      <h1>Загрузить презентацию</h1>
      <form @submit.prevent="uploadPresentation">
        <div>
          <label for="title">Название:</label>
          <input type="text" v-model="title" required />
        </div>
        <div>
          <label for="pdf_file">PDF файл:</label>
          <input type="file" @change="onFileChange" accept="application/pdf" required />
        </div>
        <button type="submit">Загрузить</button>
      </form>
      <div v-if="message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        pdf_file: null,
        message: ''
      };
    },
    methods: {
      onFileChange(event) {
        this.pdf_file = event.target.files[0];
      },
      async uploadPresentation() {
        const formData = new FormData();
        formData.append('title', this.title);
        formData.append('pdf_file', this.pdf_file);
  
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/presentations/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
              'Authorization': `Token ${localStorage.getItem('token')}` // Если вы используете токен для аутентификации
            }
          });
          this.message = 'Презентация загружена успешно!';
        } catch (error) {
          this.message = 'Ошибка загрузки: ' + error.response.data;
        }
      }
    }
  };
  </script>