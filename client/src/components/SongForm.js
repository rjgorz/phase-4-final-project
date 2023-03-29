import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'
import {useFormik} from "formik"
import { Form } from "semantic-ui-react";
import * as yup from "yup"

function SongForm({user}) {

    const history = useHistory();


    const formSchema = yup.object().shape ({
        title: yup.string().required("Please enter a user name"),
        genre: yup.string().required("Please enter a genre"),
        mp3: yup.array().min(1, "Please upload an mp3 file")
    })

    const formik = useFormik({
        initialValues: {
            title: '',
            genre: '',
            mp3: ''
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            console.log(values)
            fetch('/songs', {
                method: "POST",
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                body: JSON.stringify(values),
            })
            .then(res => {
                if(res.ok) {
                    res.json().then(() => {
                        history.push('/')
                    })
                } else {
                    res.json().then(console.log)
                }
            })
        }
    })

    return (
        <div>
          <h1>New Song Submission Form</h1>
          <Form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
            <label htmlFor="title">Title</label>
            <br />
            <input
              id="title"
              name="title"
              onChange={formik.handleChange}
              value={formik.values.title}
            />
            <p style={{ color: "red" }}> {formik.errors.title}</p>
            <label htmlFor="genre">Genre</label>
            <br />
    
            <input
              id="genre"
              name="genre"
              onChange={formik.handleChange}
              value={formik.values.genre}
            />
            <p style={{ color: "red" }}> {formik.errors.genre}</p>
    
            <label htmlFor="mp3">mp3</label>
            <br />
    
            <input
              id="mp3"
              type="file"
              name="file"
              accept=".mp3"
              onChange={(event) => formik.setFieldValue("file", event.currentTarget.files[0])}
              value={formik.values.mp3}
            />
            <p style={{ color: "red" }}> {formik.errors.mp3}</p>
            <button type="submit">Submit</button>
          </Form>
        </div>
      );
}

export default SongForm;