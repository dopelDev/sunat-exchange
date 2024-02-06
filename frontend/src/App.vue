<template>
<div id="app">
	<Header />
	<Main />
	<Footer />
	</div>
</template>


<script>
	import Header from './components/Header.vue';
	import Footer from './components/Footer.vue';
	import Main from './components/Main.vue';
export default {
name: 'App',
	components: {
		Header,
		Footer,
		Main
	},
}
</script>

<style lang="scss">
@import './assets/scss/main.scss';
</style>
