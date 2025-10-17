'use client'
import { useState } from 'react'
import { BASE_URL } from '@/store'
import "../style.scss"

function Login() {
    const [form, setForm] = useState({
        username: '',
        password: ''
    })

    async function handleSubmit(e) {
        e.preventDefault()
        try {
            const response = await fetch(BASE_URL + "/api/login/", {
                method: "POST",
                body: JSON.stringify(form),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            const data = await response.json()
            console.log(data)
            localStorage.setItem("token", data.token)
            alert("Login successful")
            router.push("/")
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
            <h1>Login</h1>
            <form onSubmit={handleSubmit} className="login-form">
                <div className="form-control">
                    <label htmlFor="username">Username</label>
                    <input type="text" name="username" id="username" onChange={handleFormInputs}/>
                </div>
                <div className="form-control">
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" id="password" onChange={handleFormInputs}/>
                </div>
                <button type="submit">Login</button>
            </form>
        </>
    );
}

export default Login;