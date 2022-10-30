import { Tensor } from "@tensorflow/tfjs-node";
import * as fs from "fs";
const tf = require("@tensorflow/tfjs-node");

export const convertImageToTensor = (path: string) => {
  try {
    const imageBuffer = fs.readFileSync(path);
    const tensor = tf.node.decodeImage(imageBuffer);
    const resizedTensor = tf.image.resizeBilinear(tensor, [300, 300]);
    const expandDimsTensor = tf.expandDims(resizedTensor, 0);

    return expandDimsTensor;
  } catch (error) {
    return null;
  }
};
