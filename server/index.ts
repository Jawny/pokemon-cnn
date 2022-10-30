// const tf = require("@tensorflow/tfjs-node-gpu");
// const tfjs = require("@tensorflow/tfjs");
import cors from "cors";
import express from "express";
import bodyParser from "body-parser";
import { inferenceRoute } from "./routes";

// const model = await tf.loadModel("./results/tfjs/model.json");

const PORT = process.env.PORT || 8000;
const app = express();

// Allow CORS
app.use(cors());

// Parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// Parse application/json
app.use(bodyParser.json());

// Add routes
app.use("/inference", inferenceRoute);

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
