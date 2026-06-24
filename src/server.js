import app from "./app.js";
import express from "express";
import initFinancialDB from "../initDb.js";

const port = process.env.PORT || 3000;

initFinancialDB();
app.listen(port, () => {
  console.log("API corriendo en puerto: ", port);
});
