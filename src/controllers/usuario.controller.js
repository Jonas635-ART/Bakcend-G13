import {conexion} from "../conexion.js";
import registroUsuarioDTO from "../dtos/usuario.dto.js";
import bcrypt from "bcrypt";
import  JsonWebToken  from "jsonwebtoken";

export const registrocontroller = async (req, res) => {
    const { error, value} = registroUsuarioDTO.validate(req.body);
    if (error) {
        return res.status(400).json({
            message:"error al crear el usuario",
            content: error.details,
        });
    }
    const hashpassword = await bcrypt.hash(value.password, 10);

    const usuarioCreado = await conexion.usuario.create({
        data: {
            ...value,
            password: hashpassword,
        },
    });

    return res.status(201).json({
        message:"usuario creado exitosamente",
        content: error.details,
    });
};

export const logincontroller = async (req, res) => {},


































