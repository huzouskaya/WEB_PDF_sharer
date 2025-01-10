<template>
    <div>
      <el-upload
        class="upload-demo"
        action="http://localhost:8000/api/pdfs/"
        :on-success="handleSuccess"
        :before-upload="beforeUpload"
        :show-file-list="false"
      >
        <el-button slot="trigger">Выберите PDF</el-button>
        <el-button type="primary" slot="upload">Загрузить</el-button>
      </el-upload>
  
      <canvas ref="pdfCanvas" style="border: 1px solid black;"></canvas>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    setup() {
      const pdfCanvas = ref<HTMLCanvasElement | null>(null);
  
      const handleSuccess = (response: any) => {
        const pdfUrl = response.fileUrl; // URL загруженного PDF
        renderPDF(pdfUrl);
      };
  
      const beforeUpload = (file: File) => {
        const isPDF = file.type === 'application/pdf';
        if (!isPDF) {
          alert('Выберите PDF файл!');
        }
        return isPDF;
      };
  
      const renderPDF = async (url: string) => {
        const loadingTask = (window as any).pdfjsLib.getDocument(url); // Используем window для доступа к pdfjsLib
        const pdf = await loadingTask.promise;
  
        const page = await pdf.getPage(1);
        const scale = 1.5;
        const viewport = page.getViewport({ scale });
  
        if (pdfCanvas.value) {
          const context = pdfCanvas.value.getContext('2d');
          pdfCanvas.value.height = viewport.height;
          pdfCanvas.value.width = viewport.width;
  
          const renderContext = {
            canvasContext: context,
            viewport: viewport,
          };
          await page.render(renderContext).promise;
        }
      };
  
      return {
        pdfCanvas,
        handleSuccess,
        beforeUpload,
      };
    },
  });
  </script>
  
  <style scoped>
  .upload-demo {
    margin-bottom: 20px;
  }
  </style>