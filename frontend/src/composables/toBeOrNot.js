import { ref, onMounted, onUnmounted } from 'vue'

export function useDeviceType() {
	const deviceType = ref('desktop');

	const checkDeviceType = () => {
		if (window.innerWidth < 1024) {
			deviceType.value = 'mobile'
		} else {
			deviceType.value = 'desktop'
		}
	};
	onMounted(() => {
		checkDeviceType();
		window.addEventListener('resize', checkDeviceType);
	});
	onUnmounted(() => {
		checkDeviceType();
		window.removeEventListener('resize', checkDeviceType);
	});
	return { deviceType };
}
