<template>
	<div class="container is-fluid p-5 color2" v-if="deviceType === 'desktop' ">
		<div class="columns is-desktop p-1 mx-4">
			<div class="column is-2">
				<input class="input is-rounded custom-placeholder color3 text-color1" type="text" placeholder="Search...            󰍉">
			</div>
			<div class="column is-8">
				<h1 class="title is-4 has-text-centered text-color4" id="rounded">Dashboard</h1>
			</div>
			<div class="column is-1 ml-6">
				<div class="columns ml-6">
					<div class="column">
						<span class="icon-text">
							<span class="icon">
								<i class="is-clickable" id="bell">  </i>
							</span>
						</span>
					</div>
					<div class="column">
						<div class="dropdown is-active" :class="{'is-active': isDropdownActive}">
							<div class="dropdown-trigger">
								<span class="icon-text">
									<span class="icon">
										<i class="is-clickable" @click="toggleDropdown" id="user">  </i>
									</span>
								</span>
							</div>
							<div v-if="isDropdownActive" class="dropdown-menu" id="dropdown-menu" role="menu">
								<div class="dropdown-content">
									<a href="#" class="dropdown-item">
										Profile
									</a>
									<a href="#" class="dropdown-item">
										Logout
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { useDeviceType } from '@/composables/global.js'
	export default {
		name: 'Header',
		data() {
			return {
				isDropdownActive: false
			}
		},
		methods: {
			toggleDropdown() {
				console.log('clicked');
				this.isDropdownActive = !this.isDropdownActive;
				console.log(this.isDropdownActive);
			}
		},
		setup() {
			const { deviceType } = useDeviceType();
			return { deviceType };
		}
	}
</script>

<style lang="scss">
* {
	font-family: '3270NerdFont-Regular';
}
.custom-placeholder::placeholder {
	font-family: '3270NerdFont-Condensed';
	font-weight: bold;
	color: #12486B !important;
}
#rounded {
	border-radius: 20px;
}
#bell {
	font-size: 1.2rem;
	color: #F5FCCD;
	font-style: normal !important;
}
#user {
	font-style: normal !important;
	font-size: 1.2rem;
	color: #F5FCCD;
}
.dropdown {
	z-index: 1000;
}
</style>
