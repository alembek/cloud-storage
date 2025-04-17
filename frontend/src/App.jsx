import { useState } from 'react'

import axios from 'axios'


function App() {

  const [file, setFile] = useState(null)


  const upload = async () => {

    const formData = new FormData()

    formData.append("file", file)

    const res = await axios.post("http://0.0.0.0:8000/upload", formData)

    alert(`Uploaded to: ${res.data.url}`)

  }


  return (

    <div>

      <h1>Cloud Storage</h1>

      <input type="file" onChange={e => setFile(e.target.files[0])} />

      <button onClick={upload}>Upload</button>

    </div>

  )

}


export default App

