import express from 'express'
import mongoose from 'mongoose'
import dotenv from 'dotenv'

dotenv.config()
const server = express()
const PORT = process.env.PORT ?? 3000

const conectarBd = async()=> {
    await mongoose.connect(process.env.MONGODB_URL)
    console.log('Conexio exitosa')
}

server.listen(PORT,async () => {
    console.log(`Servidor corriendo ${PORT}`)
    await conectarBd()
})











































