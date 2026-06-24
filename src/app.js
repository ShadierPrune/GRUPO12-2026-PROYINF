import express from "express";
import cors from "cors";
import routes from "./routes/index.js";

const app = express();


app.use(cors({
  origin: "http://localhost:5173", 
  credentials: true                
}));
app.use((req, res, next) => {
  console.log("➡️ Petición recibida en api principal:", req.method, req.url);
  next();
});

app.use(express.json());
app.use("/api", routes);

export default app;
