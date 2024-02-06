<template>
	<div class="container">
		<h1 class="title"> {{ deviceType }} Hello</h1>
	</div>
</template>

<script>
import { useDeviceType } from '@/composables/global.js'
	export default {
		name: 'Header',
		data() {},
		setup() {
			const { deviceType } = useDeviceType();
			return { deviceType };
		}
	}
</script>

<style>

</style>
