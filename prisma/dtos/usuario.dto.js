import { TipoUsuario } from "@prisma/client";
import Joi from joi;


const registroUsuarioDTO = Joi.object({
    nombre: Joi.string().required(),
    email: Joi.string().email().required(),



    password: Joi.string()
        .regex(
            new RegExp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%-*]).{6,}$")
        )
        .messages({
            "string.pattern.base":
            "el password debe tener mayusculas, minusculas, numero, caracteres especiales"
        })
        .required(),
    TipoUsuario: Joi.string()
        .valid(TipoUsuario.ADMIN, TipoUsuario.CLIENTE)
        .optional(),

})
export const loginDto = async (req, res) => {
    const {error, value} = loginDto.validate(req.body);
    if(error){
        return res.status(400).json({
            message:"error al hacer el login",
            content:error.details
        });
    }
    const usuarioEncontrado = await conexion.usuario.findUnique({
        where: { email: value.email},
    });
    if(!usuarioEncontrado){
        return res.status(400).json({
            message: "Usuario no existe en la bd"
        });
    }
    bcrypt.compare(
        value.password, 
        usuarioEncontrado.password
        );
    if(resultado === false){
        return res.status(400).json({
            message:"Contraseña invalida",
        });
    }
    const token = jsonwebtoken.sign(
        {
            sub:usuarioEncontrado.id,
            nombre: usuarioEncontrado.nombre,
        }
    )
    return res.json({
        token:"xxxxxx"
    });
};










































