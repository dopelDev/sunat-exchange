<template>
	<div class="container color3" :class="{ 'big-container': responsiveState }">
		<div class="column">
			<div class="column is-child">
				<figure>
					<img class="is-clickable" @click="toggleSize" :src="require('Assets/images/favicon.png')" alt="Placeholder image">
				</figure>
			</div>
			<div v-for="title in titles" :key="title.id" class="column is-clickable my-6">
				<h1 class="title is-4 has-text-centered text-color1">{{ title.currentText }}</h1>
			</div>
		</div>
	</div>
</template>

<script>
	import { responsiveState, useTitles } from '@/composables/global.js';
	export default {
		name: 'StickyBar',
		data() {
			return {
				resize: false
			}
		},
		setup() {
			const { titles, toggleTitleSize } = useTitles();
			const toggleSize = () => {
				responsiveState.value = !responsiveState.value;
				titles.forEach(title => {
					title.currentText = title.currentText === title.defaultText ? title.alternativeText : title.defaultText;
				});
			};
			return { responsiveState, titles, toggleSize, toggleTitleSize };
		}
	}
</script>

<style lang="scss">
.container {
	left: 0;
	justify-content: center;
	width: 100% !important; // toogle this to see the effect using the button and method
		transition: width 0.5s ease;
}
.big-container {
	justify-content: center;
	width: 180% !important;
}
.is-child {
	flex: 0 1 100px;
	margin-top: 30px;
	margin-bottom: 60px;
	text-align: center;
	padding-right: 0;
}
.title {
	white-space: pre-wrap;
}
</style>

