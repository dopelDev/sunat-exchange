import { reactive } from 'vue'

// create a share state

export function useTitles() {
	const titles = reactive([
		{ id: 1, defaultText: ' ', alternativeText: '  Overview', currentText: ' ' },
		{ id: 2, defaultText: ' ', alternativeText: '   Peaks', currentText: ' ' },
		{ id: 3, defaultText: '󰨦 ', alternativeText: '󰨦 Inflation', currentText: '󰨦 ' },
	]);

	const toggleTitleSize = (titleId) => {
		const foundTitle = titles.value.find(t => t.id === titleId);
		if (foundTitle) {
			foundTitle.currentText = foundTitle.currentText === foundTitle.defaultText ? foundTitle.alternativeText : foundTitle.defaultText;
		}
	};

	return { titles, toggleTitleSize};
};
