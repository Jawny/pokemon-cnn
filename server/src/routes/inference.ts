import express from "express";
import multer from "multer";
import { convertImageToTensor, deleteFile } from "@utils";
import { POKEMON_LABELS } from "@static";
const tf = require("@tensorflow/tfjs-node");

export const inferenceRoute = express.Router();

const upload = multer({ dest: "./uploads" });

inferenceRoute.post(
  "/classify-pokemon",
  upload.single("image"),
  async (req: any, res: any) => {
    try {
      console.log(req.file);
      const { path } = req.file;

      const model = await tf.loadGraphModel(
        "file:///home/johnny/code/pokemon-cnn/training/results/tfjs/model.json"
      );
      const tensorImage = convertImageToTensor(`./${path}`);
      const tensorPrediction = model.predict(tensorImage);
      const result = tensorPrediction.argMax(1).arraySync()[0];
      res.send({ pokemon: POKEMON_LABELS[result] });
      deleteFile(`./${path}`);
    } catch (error) {
      console.error(error);
      res.send({ error: "null" });
    }
  }
);
