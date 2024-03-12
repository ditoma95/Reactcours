/* eslint-disable react/prop-types */
import {useRef, useEffect } from 'react';

export function VideoPlayer({ src, isPlaying }) {
	const ref = useRef(null);
	useEffect(()=>{
		if (isPlaying) {
			// Ces appels sont interdits pendant le rendu.
			ref.current.play();
		} else {
			// En plus, ça plante.
			ref.current.pause();
		}
	})
	return <video ref={ref} src={src} loop playsInline />;
}
