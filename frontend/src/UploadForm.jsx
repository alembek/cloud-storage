import React, { useState } from 'react';

import axios from 'axios';


function UploadForm() {

  const [file, setFile] = useState(null);


  // Функция обработки изменения файла

  const handleFileChange = (e) => {

    setFile(e.target.files[0]);

  };


  // Функция отправки файла на сервер

  const handleUpload = async () => {

    if (!file) {

      alert('Please select a file!');

      return;

    }


    const formData = new FormData();

    formData.append('file', file);


    try {

      const response = await axios.post('http://185.182.219.45/upload/', formData, {

        headers: {

          'Content-Type': 'multipart/form-data',

        },

      });

      console.log('File uploaded successfully:', response.data);

    } catch (error) {

      console.error('Error uploading file:', error);

    }

  };


  return (

    <div>

      <h2>Upload File</h2>

      <input type="file" onChange={handleFileChange} />

      <button onClick={handleUpload}>Upload</button>

    </div>

  );

}


export default UploadForm;

