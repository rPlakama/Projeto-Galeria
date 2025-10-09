CREATE TABLE IF NOT EXISTS artistas(
  id INT AUTO_INCREMENT PRIMARY KEY,
  onde_nasceu VARCHAR(255) NOT NULL,
  nasceu_morreu VARCHAR(255) NOT NULL,
  epoca_de_trabalho VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS artes(
  id INT AUTO_INCREMENT PRIMARY KEY,
  arte VARCHAR(255) NOT NULL,
  epoca VARCHAR(255) NOT NULL,
  imagem VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS funcionarios(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  salarios VARCHAR(255) NOT NULL,
  especialidade VARCHAR(255) NOT NULL
);

  /* Gera variaveis de texto, com 255 caracteres, não vazias. */

