import Pokedex from "pokedex-promise-v2";

const options: any = {
  protocol: "https",
  hostName: "localhost:443",
  versionPath: "/api/v2/",
  cacheLimit: 100 * 1000, // 100s
  timeout: 5 * 1000, // 5s
};

const P = new Pokedex(options);
