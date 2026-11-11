import {Composition} from 'remotion';
import {Principal} from './Principal';
import {DURACAO, FPS} from './tempo';

export const RemotionRoot = () => (
  <Composition
    id="Principal"
    component={Principal}
    width={1080}
    height={1920}
    fps={FPS}
    durationInFrames={Math.ceil(DURACAO * FPS)}
  />
);
