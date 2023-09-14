import { TipoUsuario } from "@prisma/client";
import jsonwebtoken from "jsonwebtoken";

export const validarUsuario = async(req, res, next) => {
    const {authorization} = req.headers;
    if(!authorization) {
        return res.status(403).json({
            message:"SE necesita token para la peticion",
        });
    }
    
    const token = authorization.split(' ')[1]
    if(!token){
        return res.status(403).json({
            message:"el formato par enviar la token es Bearer YOUR TOKEN"
        });
    }
    try {
    const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);
    console.log(payload);

    } catch (error) {
        return res.status(403).json({
            message: "Error al validar el usuario",
            content: error.message,
        });
    }

    next();
};
export const validarUsuarioAdmin = async( req, res, next)=> {
    if(req.user.tipoUsuario === TipoUsuario.ADMIN){
        next();
    } else {
        return res.status(403).json({
            message: "No tienes los permisos"
        });
    }
};