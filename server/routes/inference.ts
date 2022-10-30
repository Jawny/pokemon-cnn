import express from "express";

export const inferenceRoute = express.Router();

inferenceRoute.post("/classify-pokemon", async (req: any, res: any) => {
  const { image } = req.body;
  console.log(image);
});

module.exports = { inferenceRoute };
