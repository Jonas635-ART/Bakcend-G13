import express from 'express';
import { listarEquipos }from "../controllers/equipo.controller.js";

export const equipoRouter = express.Router();
equipoRouter.get("/equipos", listarEquipos)























