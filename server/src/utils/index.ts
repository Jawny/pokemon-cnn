import * as fs from "fs";
const tf = require("@tensorflow/tfjs-node");

export const convertImageToTensor = (path: string) => {
  const imageBuffer = fs.readFileSync(path);
  const tensor = tf.node.decodeImage(imageBuffer);
  return tensor;
};
