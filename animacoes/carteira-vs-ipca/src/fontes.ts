import {continueRender, delayRender, staticFile} from 'remotion';

export const SERIFA = "'DM Serif Display', Georgia, serif";
export const SANS = "'Geist', 'Helvetica Neue', Arial, sans-serif";

const carregar = async () => {
  const fontes = [
    new FontFace('DM Serif Display', `url(${staticFile('fontes/DMSerifDisplay-Italic.ttf')})`, {style: 'italic'}),
    new FontFace('DM Serif Display', `url(${staticFile('fontes/DMSerifDisplay-Regular.ttf')})`, {style: 'normal'}),
    new FontFace('Geist', `url(${staticFile('fontes/Geist-Variable.ttf')})`, {weight: '100 900'}),
  ];
  await Promise.all(fontes.map(async (f) => document.fonts.add(await f.load())));
};

if (typeof document !== 'undefined') {
  const h = delayRender('fontes');
  carregar().then(() => continueRender(h));
}
