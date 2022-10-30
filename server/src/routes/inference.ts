import express from "express";
import multer from "multer";
import { convertImageToTensor } from "@utils";
const tf = require("@tensorflow/tfjs-node");

export const inferenceRoute = express.Router();

const upload = multer({ dest: "./uploads" });

inferenceRoute.post(
  "/classify-pokemon",
  upload.single("image"),
  async (req: any, res: any) => {
    const model = await tf.loadGraphModel(
      "file://../../training/results/tfjs/model.json"
    );

    const zeros = tf.zeros([1, 224, 224, 3]);

    await model.predict(zeros).print();
  }
);
