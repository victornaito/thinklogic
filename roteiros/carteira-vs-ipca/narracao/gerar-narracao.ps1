# Gera a narração com a voz treinada do Victor (F5-TTS), um arquivo por bloco.
# Rode no PowerShell, com o tts-env ativado:  .\gerar-narracao.ps1
# Não mexe no modelo nem na pasta tts-env: só lê o checkpoint.

$CKPT  = "C:\Users\VICTO\tts-env\Lib\ckpts\voz_victor\model_last.pt"
# Preencha com o mesmo áudio e texto de referência usados no treino/teste da voz:
$REF_AUDIO = "C:\caminho\para\referencia-victor.wav"
$REF_TEXT  = "texto exato que o Victor fala no áudio de referência"
# Se o treino usou um vocab próprio, aponte aqui (senão deixe vazio):
$VOCAB = ""
# F5TTS_v1_Base se o fine-tune partiu da v1; F5TTS_Base se partiu da versão antiga.
$MODEL = "F5TTS_v1_Base"

$saida = Join-Path $PSScriptRoot "audio"
New-Item -ItemType Directory -Force -Path $saida | Out-Null

Get-ChildItem (Join-Path $PSScriptRoot "bloco-*.txt") | Sort-Object Name | ForEach-Object {
  $nome = $_.BaseName
  $params = @("--model", $MODEL, "--ckpt_file", $CKPT,
            "--ref_audio", $REF_AUDIO, "--ref_text", $REF_TEXT,
            "--gen_file", $_.FullName, "--output_dir", $saida,
            "--output_file", "$nome.wav", "--remove_silence")
  if ($VOCAB -ne "") { $params += @("--vocab_file", $VOCAB) }
  Write-Host "Gerando $nome..."
  f5-tts_infer-cli @args
}
Write-Host "Pronto. Mande os arquivos de $saida no chat."
