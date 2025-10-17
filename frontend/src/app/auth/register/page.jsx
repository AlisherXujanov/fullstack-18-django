'use client'
import { useState } from 'react'
import { BASE_URL } from '@/store'
import "../style.scss"

function Register() {
    const [form, setForm] = useState({
        username: '',
        password: '',
        password2: ''
    })

    async function handleSubmit(e) {
        e.preventDefault()
        try {
            const response = await fetch(BASE_URL + "...", {
                metthod: "POST",
                body: JSON.stringify(form),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            const data = await response.json()
            console.log(data)
            console.log(data.token)
        } catch (e) {
            console.log(e)
        }
    }

    function handleFormInputs(e) {
        const {name, value} = e.target
        setForm({
            ...form,
            [name]: value
        })
    }

    return (
        <>
            <h1>Register</h1>
            <form onSubmit={handleSubmit} className="register-form">
                <div className="form-control">
                    <label htmlFor="username">Username</label>
                    <input type="text" name="username" id="username" onChange={handleFormInputs}/>
                </div>
                <div className="form-control">
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" id="password" onChange={handleFormInputs}/>
                </div>
                <div className="form-control">
                    <label htmlFor="password2">Password confirmation</label>
                    <input type="password" name="password2" id="password2" onChange={handleFormInputs}/>
                </div>
                <button type="submit">Register</button>
            </form>
        </>
    );
}

export default Register;